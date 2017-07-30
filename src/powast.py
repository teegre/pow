#ast.py: [PowerText] language Abstract Syntactic Tree
# _*_ coding:utf8 _*_

import operator
import math
from types import LambdaType
from typedef import *
from os.path import isfile
from symbols import Symbols
from exceptions import *
from sys import stdin, stdout
from random import random, shuffle
from time import time, sleep

symbols = Symbols()

isvariable = symbols.is_variable
isfunction = symbols.is_function
TRACE = False

class StatementList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children
    def __repr__(self):
        return f'[statements: {self.children}]'
    def __getitem__(self, index):
        return self.children[index]
    def __len__(self):
        return len(self.children)
    def __iter__(self):
        return iter(self.children)
    def eval(self):
        result = []
        for statement in self:
            if isinstance(statement, Exit):
                return statement
            evaluated = statement.eval()
            if isinstance(evaluated, Exit):
                return evaluated
            if evaluated is not None:
                result.append(evaluated)
        return result

class Variable(Base):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'var: {self.name}'
    def eval(self):
        return symbols.get_variable(self.name)

class Echo(Base):
    def __init__(self, params=None):
        self.params = params
    def __repr__(self):
        return f'[echo: {self.params}]'
    def pprint(self, *elements):
        out = ''.join([str(item) for item in elements])
        stdout.write(out)
        stdout.flush()
        return out
    def eval(self):
        result = []
        if self.params is None: print()
        else:
            for item in self.params:
                if item is not None:
                    self.pprint(str(item.eval()))
            return ''.join([str(item) for item in result])

class Get(Base):
    def __init__(self, iterable, start, end=Null()):
        self.iterable = iterable
        self.start = start
        self.end = end
    def __repr__(self):
        return f'({self.iterable}:{self.start})'
    def eval(self):
        try:
            if isnull(self.end):
                return self.iterable.eval()[self.start.eval()]
            return self.iterable.eval()[self.start.eval():self.end.eval()]
        except TypeError:
            raise PowTypeError(f'*** ({self.iterable.eval().powtype()}:{self.start.eval().powtype()}) type error')

class Set(Base):
    def __init__(self, name, value, index=None):
        self.name = name
        self.value = value
        self.index = index
    def __repr__(self):
        return f'[set: {self.name}<-{self.value}]'
    def __iter__(self):
        return iter(self.value)
    def eval(self):
        value = self.value
        if self.index is None:
            if isinstance(value.eval(), List):
                result = symbols.set_variable(self.name, value.eval().copy())
            else:
                result = symbols.set_variable(self.name, value.eval())
        else:
            result = symbols.set_item(self.name, self.index.eval(), value.eval())
        return result

class Del(Base):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'[del: {self.name}]'
    def eval(self):
        if symbols.is_function(self.name):
            return symbols.del_function(self.name)
        else:
            return symbols.del_variable(self.name)

class MakeList(Base):
    def __init__(self, items):
        self.items = items
    def __repr__(self):
        return f'[makelist: {tuple(self.items)}]'
    def eval(self):
        new_list = List()
        for item in self.items:
            new_list.push(item.eval())
        return new_list

class Push(Base):
    def __init__(self, _list, value):
        self.list = _list
        self.value = value
    def __repr__(self):
        return f'push: {self.list}<-{self.value}'
    def eval(self):
        _list = self.list.eval()
        try:
            for value in self.value:
                _list.push(value.eval())
            return _list
        except AttributeError as e:
            print('*** push: list expected.', e)
            return _list
        except Exception as e: raise PowRuntimeError(e)

class Head(Base):
    def __init__(self, _list):
        self.list = _list
    def __repr__(self):
        return f'[head: {self.list}]'
    def eval(self):
        return self.list.eval().head()

class Tail(Base):
    def __init__(self, _list):
        self.list = _list
    def __repr__(self):
        return f'[tail: {self.list}]'
    def eval(self):
        return self.list.eval().tail()

class Last(Base):
    def __init__(self, _list):
        self.list = _list
    def __repr__(self):
        return f'[tail: {self.list}]'
    def eval(self):
        return self.list.eval().last()

class Len(Base):
    def __init__(self, item):
        self.item = item
    def __repr__(self):
        return f'[len: {self.item}]'
    def eval(self):
        return len(self.item.eval())

def filter_list(expr, _list):
    if isnull(_list): return _list
    filtered = filter_list(expr, _list.tail())
    if istrue(expr.eval([ttype(_list.head())])):
        return List(_list.head(), filtered)
    else:
        return filtered

class Filter(Base):
    def __init__(self, expr, _list):
        self.expr = expr
        self.list = _list
    def __repr__(self):
        return f'[filter: {self.expr}->{self.list}]'
    def eval(self):
        _list = self.list.eval()
        if not isinstance(_list, List):
            raise PowTypeError(f'*** filter: list expected, got {ttype(_list).powtype()}')
        return filter_list(self.expr, _list)

def map_list(expr, _list):
    if isnull(_list): return _list
    if _list.isempty(): return _list
    return List(expr.eval([ttype(_list.head())]), map_list(expr, _list.tail()))

class Map(Base):
    def __init__(self, expr, _list):
        self.expr = expr
        self.list = _list
    def __repr__(self):
        return f'[map: {self.expr}->{self.list}]'
    def eval(self):
        _list = self.list.eval()
        if not isinstance(_list, List):
            raise PowTypeError(f'*** map: list expected, got {ttype(_list).powtype()}')
        return map_list(self.expr, _list)

class BinOp(Base):
    __op = {
            '+'   : operator.add,
            '-'   : operator.sub,
            '*'   : operator.mul,
            '/'   : operator.truediv,
            '%'   : operator.mod,
            '='   : operator.eq,
            '!='  : operator.ne,
            '>'   : operator.gt,
            '>='  : operator.ge,
            '<'   : operator.lt,
            '<='  : operator.le,
            '***' : operator.pow,
            '//'  : lambda a, b: int(a.eval() // b.eval()),
    }
    def __init__(self, op, a, b):
        self.a  = a
        self.b  = b
        self.op = op
    def __repr__(self):
        return f'[{self.op}: {self.a} {self.b}]'
    def eval(self):
        try:
            a, b = self.a, self.b
            op = self.__op[self.op]
            if isinstance(op, LambdaType):
                return op(a, b)
            else:
                if self.op in '+-****/\%': return op(a.eval(), b.eval())
                else: return Bool(op(a.eval(), b.eval()))
        except TypeError:
            raise PowTypeError(f'*** {self.op} < {a.eval()} > < {b.eval()} >: unable to perform operation.')
            return Null()
        #except Exception as e: raise PowRuntimeError(e)
    @property
    def value(self):
        return self.eval()

class Pow2(Base):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'[**: {self.value}]'
    def eval(self):
        return operator.pow(self.value.eval(), 2)

class Or(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[or: {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval().value
        if isinstance(b, Bool): b = b.eval().value
        return Bool(a or b)

class And(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[and: {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval().value
        if isinstance(b, Bool): b = b.eval().value
        return Bool(a and b)

class XOr(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[xor: {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval().value
        if isinstance(b, Bool): b = b.eval().value
        return Bool(operator.xor(a, b))

class Not(Base):
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return f'[not: {self.a}]'
    def eval(self):
        a = self.a.eval()
        if isinstance(a, Bool): a = a.eval().value
        return Bool(not a)

class Negative(Base):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'-{self.value}'
    def eval(self):
        try:
            return -self.value.eval()
        except TypeError:
            raise PowTypeError(f'*** -{self.value}: number expected, got {self.value.powtype}')
        except Exception as e: raise PowRuntimeError(e)

class IncDec(Base):
    def __init__(self, op, name):
        self.op = op
        self.name = name
    def __repr__(self):
        return f'[{self.op}: {self.name}]'
    def eval(self):
        value = symbols.get_variable(self.name)
        if value is not None:
            try:
                if self.op == '++': value += 1
                else: value -= 1
                return symbols.set_variable(self.name, value)
            except TypeError:
                raise PowTypeError('*** {self.op}: number expected, got {self.value.powtype}')
                return Null()
            except Exception as e: raise PowRuntimeError(e)

class Rnd(Base):
    def __repr__(self):
        return f'[rnd]'
    def eval(self):
        return random()

class Time(Base):
    def __repr__(self):
        return f'[time]'
    def eval(self):
        return time()

class Pause(Base):
    def __init__(self, duration):
        self.duration = duration
    def __repr__(self):
        return f'[pause: {self.duration}]'
    def eval(self):
        sleep(self.duration.eval())

class If(Base):
    def __init__(self, condition, dothis, dothat):
        self.condition = condition
        self.dothis = dothis
        self.dothat = dothat
    def __repr__(self):
        if self.dothat is not None:
            return f'[?: [{self.condition}]: {self.dothis}; {self.dothat}]'
        else:
            return f'[?: [{self.condition}]: {self.dothis}]'
    def eval(self):
        if istrue(self.condition.eval()):
            result = self.dothis.eval()
            if isinstance(result, Exit):
                return result
            try: return result[-1]
            except: return Null()
        elif self.dothat is not None:
            result = self.dothat.eval()
            if isinstance(result, Exit):
                return result
            try: return result[-1]
            except: return Null()

class Exit(Base):
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return []
    def __repr__(self):
        if self.value:
            return f'[exit: {self.value}]'
        else: return '[exit]'
    def eval(self):
        return self.value.eval()

class While(Base):
    def __init__(self, condition, dothis):
        self.condition = condition
        self.dothis = dothis
    def __repr__(self):
        return f'[while: condition [{self.condition}]: body={self.dothis}]'
    def eval(self):
        try:
            while istrue(self.condition.eval()):
                result = self.dothis.eval()
                if isinstance(result, Exit):
                    return result.eval()
        except KeyboardInterrupt:
            print()
            print('*** while: interrupted by user')

class For(Base):
    def __init__(self, var, a, b, step, dothis):
        self.var = var
        self.a = a
        self.b = b
        self.step = step
        self.dothis = dothis
    def __repr__(self):
        return('[for: [{self.var} {self.a} {self.b} {self.step}]]')
    def eval(self):
        try:
            a = self.a
            b = self.b
            step = self.step
            body = self.dothis
            var = self.var
            setvar = Set(var, a)
            i = a
            if a.eval() > b.eval(): op = '>='
            else: op = '<='
            while istrue(BinOp(op, i, b).eval()):
                setvar.eval()
                result = body.eval()
                if isinstance(result, Exit):
                    print('if:', result)
                    return result
                setvar = Set(var, BinOp('+', i, step))
                i = BinOp('+', i, step)
        except KeyboardInterrupt:
            print()
            print('*** for: interrupted by user')

class Def(Base):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f'[def: {self.name} {self.params}: {self.body}]'
    def eval(self):
        symbols.set_function(self.name, self.params, self.body)
        return f'[{self.name}]'

class FunctionCall(Base):
    def __init__(self, name, params):
        self.name = name
        self.params = params
    def __repr__(self):
        return f'[function call: [{self.name} {self.params}]]'
    def eval(self):
        func = symbols.get_function(self.name)
        if func is None: return Null()
        params = func[0]
        if len(params) != len(self.params):
            raise InvalidParamCount(f'*** {self.name}: invalid number of parameters.\n*** expected {len(params)}, got {len(self.params)}')
            return Null()
        sparams = [param.eval() for param in self.params]
        body = func[1]
        symbols.set_local()
        symbols.set_localfunction()
        if TRACE:
            print('function:', self.name, self.params)
            print('         ', params)
        for index, param in enumerate(params):
            result = symbols.set_variable(param, sparams[index])
            if TRACE:
                print('source:', type(sparams[index]), sparams[index])
                print('dest  :', param)
        try:
            result = body.eval()
            try: result = result.eval()
            except: pass
            if TRACE: print('\tstatement:', body, '\n', '\tresult:', result)
            return result[-1]
        except PowException as e : print(e)
        finally: symbols.del_local()

class LambdaCall(Base):
    def __init__(self, f, params):
        self.f = f
        self.params = params
    def __repr__(self):
        return f'[lambda call: {self.f} {self.params}]'
    def eval(self, params=None):
        if params is not None: self.params = params
        if TRACE: print(self)
        f = self.f.eval()
        sparams = [param.eval() for param in self.params]
        if not islambda(f):
            raise UndefinedFunction('*** not a lambda expression')
        if len(self.params) != len(f.params):
            raise InvalidParamCount(f'*** lambda: invalid number of parameters.\n*** expected {len(f.params)}, got {len(self.params)}')
        symbols.set_local()
        symbols.set_localfunction()
        for index, param in enumerate(f.params):
            symbols.set_variable(param, sparams[index])
        result = f.body.eval()
        try: result = result.eval()
        except: pass
        symbols.del_local()
        return result

#class StandardFunction(Base):
#    def  __init__(self, func):
#        self.func = func
#    def __repr__(self):
#        return f'[standard function: {self.func}]'
#    def eval(self):

class Uses(Base):
    def __init__(self, module, parser):
        self.module = module
        self.parser = parser
    def __repr__(self):
        return f'[use: {self.module}]'
    def eval(self):
        if TRACE: print(self)
        module = self.module + '.pow'
        if isfile(module):
            with open(module, 'r') as f:
                lines = ''.join(f.readlines())
            instructions = self.parser.parse(lines)
            instructions.eval()
        else:
            print(f'*** use: module {self.module} not found.')
            return Null()

class ScreenSize(Base):
    def __repr__(self):
        return '[screensize]'
    def eval(self):
        from os import get_terminal_size
        size = get_terminal_size(stdout.fileno())
        return List(size.lines, List(size.columns))

class GetCursor(Base):
    def __repr__(self):
        return '[getcursor]'
    def eval(self):
        """Get cursor position."""
        from termios import tcgetattr, tcsetattr, CREAD, ECHO, ICANON, TCSADRAIN
        import os
        tty = os.ttyname(stdin.fileno())
        fd = os.open(tty, os.O_RDWR + os.O_NOCTTY)
        cflag, lflag = 2, 3
        saved = tcgetattr(fd)
        temp = tcgetattr(fd)
        temp[lflag] = temp[lflag] & ~ICANON
        temp[lflag] = temp[lflag] & ~ECHO
        temp[cflag] = temp[cflag] & ~CREAD
        try:
            tcsetattr(fd, TCSADRAIN, temp)
            os.write(fd, b'\x1b[6n')
            result = os.read(fd, 9)
        except Exception: raise PowRuntimeError('*** runtime error')
        finally:
            tcsetattr(fd, TCSADRAIN, saved)
            os.close(fd)
            result = result.decode()
            result = result[2:]
            result = result.split(';')
            y = int(result[0])
            x = int(result[1][:-1])
        return List(y, List(x))
