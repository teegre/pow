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
from time import time, strftime, sleep

symbols = Symbols()

isvariable = symbols.is_variable
isfunction = symbols.is_function

class StatementList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children
    def __repr__(self):
        return f'{self.children}'
    def __getitem__(self, index):
        return self.children[index]
    def __len__(self):
        return len(self.children)
    def __iter__(self):
        return iter(self.children)
    def eval(self):
        result = []
        for statement in self:
            if isinstance(statement, Skip):
                return statement
            if isinstance(statement, Exit):
                return statement
            evaluated = statement.eval()
            if isinstance(evaluated, Skip):
                return evaluated
            if isinstance(evaluated, Exit):
                return evaluated
            if evaluated is not None:
                result.append(evaluated)
        return result

class Variable(Base):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'var {self.name}'
    def eval(self):
        return symbols.get_variable(self.name)

class Echo(Base):
    def __init__(self, params=None):
        self.params = params
    def __repr__(self):
        return f'[echo {self.params}]'
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

class Read(Base):
    def __init__(self, prompt=Null()):
        self._value = ''
        self.prompt = prompt
    def __repr__(self):
        return f'[read]'
    def pprint(self, *elements):
        stdout.write(out)
        stdout.flush()
        return out
    def eval(self):
        try:
            if not isnull(self.prompt):
                prompt = ''.join([str(item.eval()) for item in self.prompt])
            else: prompt = ''
            self._value = ttype(input(prompt))
            return self._value
        except KeyboardInterrupt:
            print()
            print('*** read: interrupted by user')
            return Exit(Null())


class Expect(Base):
    def __init__(self, _type, value):
        self.type = _type
        self._value = value
    def repr(self):
        return f'[expect: {self.type}]'
    def eval(self):
        Base._EXPECTMODE = True
        value = self._value.eval()
        if ttype(value)._type == self.type: return value
        else: return Null()

class Get(Base):
    def __init__(self, iterable, index):
        self.iterable = iterable
        self.index = index
    def __repr__(self):
        return f'({self.iterable}:{self.index})'
    def eval(self):
        try: return self.iterable.eval()[self.index.eval()]
        except TypeError:
            raise PowTypeError(f'*** type error:\n\
*** expected (list:number)\n\
*** got ({ttype(self.iterable.eval()).powtype()}:{ttype(self.index.eval()).powtype()})')
        except IndexError:
            raise PowRuntimeError(f'*** invalid index: < {self.index.eval()} >')

class Set(Base):
    def __init__(self, name, value, index=None, isglobal=False):
        self.name = name
        self._value = value
        self.index = index
        self.isglobal = isglobal
    def __repr__(self):
        return f'[set {self.name}<-{self._value}]'
    def __iter__(self):
        return iter(self._value)
    def eval(self):
        value = self._value.eval()
        if self.index is None:
            if isinstance(value, List):
                result = symbols.set_variable(self.name, value.copy(), is_global=self.isglobal)
            else:
                result = symbols.set_variable(self.name, value, is_global=self.isglobal)
        else:
            result = symbols.set_item(self.name, self.index.eval(), value)
        return result

class Del(Base):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'[del {self.name}]'
    def eval(self):
        if symbols.is_function(self.name):
            return symbols.del_function(self.name)
        else:
            return symbols.del_variable(self.name)

class MakeList(Base):
    _type = 'list'
    def __init__(self, items):
        self.items = items
    def __repr__(self):
        return f'[list {tuple(self.items)}]'
    def eval(self):
        new_list = List()
        for item in self.items:
            new_list.push(item.eval())
        return new_list

class Push(Base):
    def __init__(self, _list, value):
        self.list = _list
        self._value = value
    def __repr__(self):
        return f'[push {self.list}<-{self._value}]'
    def eval(self):
        _list = self.list.eval()
        try:
            for value in self._value:
                _list.push(value.eval())
            return _list
        except AttributeError:
            raise PowTypeError(f'*** push: list expected, got {self.list.powtype()}')
            return _list
        except Exception as e: raise PowRuntimeError(e)

class Pop(Base):
    def __init__(self, _list, index=Null()):
        self.list = _list
        self.index = index
    def __repr__(self):
        return f'[pop {self.list}->{self.index}]'
    def eval(self):
        _list = self.list.eval()
        try:
            return _list.pop(self.index.eval())
        except AttributeError:
            raise PowTypeError(f'*** pop: list expected, got {self.list.powtype()}')

class Head(Base):
    def __init__(self, _list):
        self.list = _list
    def __repr__(self):
        return f'[head {self.list}]'
    def eval(self):
        try: return self.list.eval().head()
        except AttributeError:
            raise PowTypeError(f'*** head: list expected, got {self.list.powtype()}')

class Tail(Base):
    def __init__(self, _list):
        self.list = _list
    def __repr__(self):
        return f'[tail {self.list}]'
    def eval(self):
        try: return self.list.eval().tail()
        except AttributeError:
            raise PowTypeError(f'*** tail: list expected, got {self.list.powtype()}')

class Len(Base):
    def __init__(self, item):
        self.item = item
    def __repr__(self):
        return f'[len {self.item}]'
    def eval(self):
        try: return len(self.item.eval())
        except TypeError:
            raise PowTypeError(f'*** len: {self.item.powtype()} has no length')

class ToStr(Base):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'[tostr {self._value}]'
    def eval(self):
        if isinstance(self._value, (Variable, FunctionCall, LambdaCall)):
            value = ttype(self._value.eval())
        else: value = self._value
        return value.tostr()

class ToNum(Base):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'[tonum {self._value}]'
    def eval(self):
        if isinstance(self._value, (Variable, FunctionCall, LambdaCall)):
            value = ttype(self._value.eval())
        else: value = self._value
        return value.tonum()

def filter_list(expr, _list):
    if isnull(_list): return _list
    filtered = filter_list(expr, _list.tail())
    if expr.eval([ttype(_list.head())]):
        return List(_list.head(), filtered)
    else:
        return filtered

class Filter(Base):
    def __init__(self, expr, _list):
        self.expr = expr
        self.list = _list
    def __repr__(self):
        return f'[filter {self.expr}->{self.list}]'
    def eval(self):
        _list = self.list.eval()
        if not isinstance(_list, List):
            raise PowTypeError(f'*** filter: list expected, got {ttype(_list).powtype()}')
        return filter_list(self.expr, _list)

def map_list(expr, _list):
    if isnull(_list): return _list
    return List(expr.eval([ttype(_list.head())]), map_list(expr, _list.tail()))

class Map(Base):
    def __init__(self, expr, _list):
        self.expr = expr
        self.list = _list
    def __repr__(self):
        return f'[map {self.expr}->{self.list}]'
    def eval(self):
        _list = self.list.eval()
        if not isinstance(_list, List):
            raise PowTypeError(f'*** map: list expected, got {ttype(_list).powtype()}')
        return map_list(self.expr, _list)

class Type(Base):
    def __init__(self, item):
        self.item = item
    def __repr__(self):
        return f'[type {self.item}]'
    def eval(self):
        if isinstance(self.item, Variable):
            return ttype(self.item.eval()).powtype()
        else: return ttype(self.item).powtype()

class BinOp(Base):
    __op = {
            '+'   : operator.add,
            '-'   : operator.sub,
            '*'   : operator.mul,
            '/'   : operator.truediv,
            '//'  : operator.floordiv,
            '%'   : operator.mod,
            '='   : operator.eq,
            '!='  : operator.ne,
            '>'   : operator.gt,
            '>='  : operator.ge,
            '<'   : operator.lt,
            '<='  : operator.le,
            '***' : operator.pow,
    }
    def __init__(self, op, a, b):
        self.a  = a
        self.b  = b
        self.op = op
    def __repr__(self):
        return f'[{self.op} {self.a} {self.b}]'
    def eval(self):
        try:
            a = self.a
            b = self.b
            op = self.__op[self.op]
            if self.op == '//': return int(op(a.eval(), b.eval()))
            return op(a.eval(), b.eval())
        except TypeError:
            raise PowTypeError(f'*** {self.op} < {a} > < {b} >: unable to perform operation.')
            return Null()
        #except Exception as e: raise PowRuntimeError(e)
    @property
    def value(self):
        return self.eval()

class Pow2(Base):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'[** {self.value}]'
    def eval(self):
        return operator.pow(self.value.eval(), 2)

class Or(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[or {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval()
        if isinstance(b, Bool): b = b.eval()
        return a or b

class And(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[and {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval()
        if isinstance(b, Bool): b = b.eval()
        return a and b

class XOr(Base):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'[xor {self.a} {self.b}]'
    def eval(self):
        a = self.a.eval()
        b = self.b.eval()
        if isinstance(a, Bool): a = a.eval()
        if isinstance(b, Bool): b = b.eval()
        return operator.xor(a, b)

class Not(Base):
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return f'[not {self.a}]'
    def eval(self):
        a = self.a.eval()
        if isinstance(a, Bool): a = a.eval()
        return not a

class Negative(Base):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'-{self.value}'
    def eval(self):
        try:
            if isinstance(self.value, (Variable, Number)): value = self.value.eval()
            else: value = self.value
            return -value
        except TypeError:
            raise PowTypeError(f'*** -{self.value}: number expected, got {self.value.powtype}')
        except Exception as e: raise PowRuntimeError(e)

class IncDec(Base):
    def __init__(self, op, name):
        self.op = op
        self.name = name
    def __repr__(self):
        return f'[{self.op} {self.name}]'
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
        tz = int(strftime('%z'))
        tzh = tz // 100
        tzm = tz % 100
        return time() + (tzh * 3600) + (tzm * 60)

class Char(Base):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'[char {self._value}]'
    def eval(self):
        try: return chr(self._value.eval())
        except TypeError:
            raise PowTypeError(f'*** char: number expected, got {self._value.powtype()}')

class Ord(Base):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'[ord {self._value}]'
    def eval(self):
        try: return ord(self._value.eval())
        except TypeError:
            raise PowTypeError(f'*** ord: string of length 1 expected, got {self._value.powtype()}')

class Pause(Base):
    def __init__(self, duration):
        self.duration = duration
    def __repr__(self):
        return f'[pause {self.duration}]'
    def eval(self):
        sleep(self.duration.eval())
        return Null()

class If(Base):
    def __init__(self, condition, dothis, dothat):
        self.condition = condition
        self.dothis = dothis
        self.dothat = dothat
    def __repr__(self):
        if self.dothat is not None:
            return f'[? {self.condition}: {self.dothis}; {self.dothat}]'
        else:
            return f'[? {self.condition}: {self.dothis}]'
    def eval(self):
        if self.condition.eval():
            result = self.dothis.eval()
            if isinstance(result, (Exit, Skip)):
                return result
            try: return result[-1]
            except: return Null()
        elif self.dothat is not None:
            result = self.dothat.eval()
            if isinstance(result, (Exit, Skip)):
                return result
            try: return result[-1]
            except: return Null()

class Exit(Base):
    def __init__(self, value):
        self._value = value
    def __iter__(self):
        return []
    def __repr__(self):
        if self._value:
            return f'[exit {self.value}]'
        else: return '[exit]'
    def eval(self):
        return self._value.eval()

class Skip(Base):
    def __repr__(self):
        return '[skip]'
    def __iter__(self):
        return []
    def eval(self):
        return Null()

class While(Base):
    def __init__(self, condition, dothis):
        self.condition = condition
        self.dothis = dothis
    def __repr__(self):
        return f'[while {self.condition}: {self.dothis}]'
    def eval(self):
        try:
            while self.condition.eval():
                result = self.dothis.eval()
                if isinstance(result, Skip):
                    continue
                if isinstance(result, Exit):
                    return result.eval()
        except KeyboardInterrupt:
            print()
            raise PowInterrupt('*** while: interrupted by user')

class For(Base):
    def __init__(self, var, a, b, step, dothis):
        self.var = var
        self.a = a
        self.b = b
        self.step = step
        self.dothis = dothis
    def __repr__(self):
        return(f'[for {self.var} {self.a} {self.b} {self.step}: {self.dothis}]')
    def eval(self):
        try:
            a = self.a
            b = self.b
            step = self.step
            body = self.dothis
            var = self.var
            setvar = Set(var, a)
            i = a
            if a.eval() == b.eval(): op = '='
            elif a.eval() >= b.eval(): op = '>='
            else: op = '<='
            while BinOp(op, i, b).eval():
                setvar.eval()
                result = body.eval()
                if isinstance(result, Skip):
                    continue
                if isinstance(result, Exit):
                    return result.eval()
                setvar = Set(var, BinOp('+', i, step))
                i = BinOp('+', i, step)
            return result[-1]
        except KeyboardInterrupt:
            print()
            raise PowInterrupt('*** for: interrupted by user')
        finally:
            if not symbols.islocal(): Del(var).eval()

class Is(Base):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'[?? {self._value}]'
    def eval(self):
        return is_(self._value.eval())


class Def(Base):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f'[def {self.name} {self.params}: {self.body}]'
    def eval(self):
        symbols.set_function(self.name, self.params, self.body)
        return f'[{self.name}]'

class FunctionCall(Base):
    _type = 'function'
    def __init__(self, name, params):
        self.name = name
        self.params = params
    def __repr__(self):
        return f'[{self.name} {self.params}]'
    def eval(self):
        func = symbols.get_function(self.name)
        params = func[0]
        if len(params) != len(self.params):
            raise InvalidParamCount(f'*** {self.name}: invalid number of parameters.\n*** expected {len(params)}, got {len(self.params)}')
            return Null()
        sparams = [param.eval() for param in self.params]
        body = func[1]
        symbols.set_local()
        for index, param in enumerate(params):
            result = symbols.set_variable(param, sparams[index])
        try:
            result = body.eval()
            try: result = result.eval()
            except: pass
            try: return result[-1]
            except: return result
        except PowException as e : print(e)
        finally: symbols.del_local()

class LambdaCall(Base):
    _type = 'lambda'
    def __init__(self, f, params):
        self.f = f
        self.params = params
    def __repr__(self):
        return f'[@{self.f} {self.params}]'
    def eval(self, params=None):
        if params is not None: self.params = params
        f = self.f.eval()
        sparams = [param.eval() for param in self.params]
        if not islambda(f):
            raise UndefinedFunction('*** not a lambda expression')
        if len(self.params) != len(f.params):
            raise InvalidParamCount(f'*** lambda: invalid number of parameters.\n*** expected {len(f.params)}, got {len(self.params)}')
        symbols.set_local()
        for index, param in enumerate(f.params):
            symbols.set_variable(param, sparams[index])
        try:
            result = f.body.eval()
            try: result = result.eval()
            except: pass
            return result
        except KeyboardInterrupt:
            raise PowInterrupt('*** lambda: interrupted by user')
        finally:
            symbols.del_local()

class Uses(Base):
    def __init__(self, module, parser):
        self.module = module
        self.parser = parser
    def __repr__(self):
        return f'[uses {self.module}]'
    def eval(self):
        try:
            module = self.module + '.pow'
            if isfile(module):
                with open(module, 'r') as f:
                    lines = ''.join(f.readlines())
                instructions = self.parser.parse(lines)
                instructions.eval()
            else:
                raise PowModuleNotFound(f'*** uses: module {self.module} not found.')
        except Exception as e:
            print(e)
            return Null()

class ScreenSize(Base):
    def __repr__(self):
        return '[scrsize]'
    def eval(self):
        from os import get_terminal_size
        size = get_terminal_size(stdout.fileno())
        return List(size.lines, List(size.columns))

class GetCursor(Base):
    def __repr__(self):
        return '[getcur]'
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
