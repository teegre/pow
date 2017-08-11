# typedef.py: [PowerText] type definition
# _*_ coding:utf8 _*_
from exceptions import *

class Base:
    _type = 'base'
    _EXPECTMODE = False
    def eval(self):
        raise NotImplementedError
    def tostr(self):
        if self.powtype() == 'base':
            value = ttype(self.eval())._value
        else: value = self._value
        try: return str(value)
        except:
            if not self._EXPECTMODE:
                raise PowTypeError(f'*** type error: cannot convert < {value} > to string')
            else: return Null()
        finally:
            Base._EXPECTMODE = False
    def tonum(self):
        if self.powtype() == 'base':
            value = self.eval()._value
        else: value = self._value
        try: return int(value)
        except:
            try: return float(value)
            except:
                if not self._EXPECTMODE:
                    raise PowTypeError(f'*** type error: cannot convert < {value} > to number')
                else: return Null()
        finally:
            Base._EXPECTMODE = False
    def powtype(self):
        return self._type

class Number(Base):
    _type = 'number'
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)
    def __str__(self):
        return str(self._value)
    def eval(self):
        return self._value

class String(Base):
    _type = 'string'
    def __init__(self, value):
        self._value = value
    def __repr__(self):
       return f'"{self._value}"'
    def __str__(self):
        return self._value
    def __len__(self):
        return len(self._value)
    def __iter__(self):
        return iter(self._value)
    def __getitem__(self, index):
        return self._value[index]
    def eval(self):
        return self._value

class Bool(Base):
    _type = 'bool'
    def __init__(self, value):
        if value != 0: self._value = True
        else: self._value = False
    def __repr__(self):
        return 'bool: ' + str(self._value).lower()
    def __str__(self):
        return str(self._value).lower()
    def tostr(self):
        return str(self._value).lower()
    def tonum(self):
        if self._value: return 1
        else: return 0
    def eval(self):
        return self._value

class Null(Base):
    _type = 'null'
    def __init__(self):
        self._value = '\0'
    def __getitem__(self, index):
        return self
    def __setitem__(self, index, value):
        return self
    def __repr__(self):
        return 'null'
    def __str__(self):
        return self._value
    def __len__(self):
        return 0
    def __eq__(self, other):
        return isinstance(other, Null)
    def __ne__(self, other):
        return not isinstance(other, Null)
    def __gt__(self, other):
        return False
    def __ge__(self, other):
        if isinstance(other, Null): return True
        else: return False
    def __lt__(self, other):
        return False
    def __le__(self, other):
        if isinstance(other, Null): return True
        else: return False
    def eval(self):
        return self

def listrepr(s):
    tail = ''
    if not isnull(s.tail()):
        tail = ', ' + listrepr(s.tail())
    return f'{repr(s.head())}{tail}'

def addlist(s, t):
    if isnull(s): return t
    elif s.isempty(): return t
    else: return List(s.head(), addlist(s.tail(), t))

class List(Base):
    """List type from scratch"""
    _type = 'list'
    def __init__(self, head=Null(), tail=Null()):
        assert isnull(tail) or isinstance(tail, List)
        self.__head = head
        self.__tail = tail
        self._value = self
    def __repr__(self):
        return f'( {listrepr(self)} )'
    def __getitem__(self, start, end=Null()):
        if isnull(end):
            if start == 0: return self.__head
            else: return self.__tail[start-1]
        if start == 0: return self.__head + self.__tail[:end]
        else: return self.__tail[start:end-1]
    def __setitem__(self, index, value):
        if index == 0: self.__head = value
        else: self.__tail[index-1] = value
        return value
    def __len__(self):
        if isnull(self.__head): return 0 + len(self.__tail)
        return 1 + len(self.__tail)
    def __add__(self, other):
        return addlist(self, other)
    def __eq__(self, other):
        if not isinstance(other, List): return False
        return self.__head == other.__head and self.__tail == other.__tail
    def __ne__(self, other):
        if not isinstance(other, List): return True
        return self.__head != other.__head and self.__tail != other.__tail
    def __gt__(self, other):
        if not isinstance(other, List): return False
        return self.__head > other.__head or self.__tail > other.__tail
    def __ge__(self, other):
        if not isinstance(other, List): return False
        return self.__head >= other.__head and self.__tail >= other.__tail
    def __lt__(self, other):
        if not isinstance(other, List): return False
        return self.__head < other.__head and self.__tail < other.__tail
    def __le__(self, other):
        if not isinstance(other, List): return False
        return self.__head <= other.__head and self.__tail <= other.__tail
    def tostr(self):
        #really??
        raise PowTypeError("*** cannot convert < list > to a string")
    def head(self):
        return self.__head
    def tail(self):
        return self.__tail
    def last(self):
        if isnull(self.__head): return self
        tail = self.__tail
        while not isnull(tail):
            if isnull(tail.tail()):
                return tail
            tail = tail.tail()
        return self
    def push(self, item):
        if self.isempty(): self.__head = item
        else:
            last_list = self.last()
            last_list.__tail = List(item)
        return self
    def pop(self, index=Null()):
        if isnull(self.__head) or index > len(self) - 1: return Null()
        if index == 0:
            if isnull(self.__tail):
                head = self.__head
                self.__head = Null()
                return head
            head = self.__head
            tail = self.__tail
            self.__tail = tail.__tail
            self.__head = tail.__head
            return head
        elif isnull(index):
            index = len(self) - 1
        current = self.__tail
        idx = 0
        tail = List(self.__head)
        while idx < index - 1:
            tail += List(current.__head)
            current = current.__tail
            idx += 1
        if isnull(current):
            head = tail
            self.__head = Null()
            return head
        head = current.__head
        self.__head = tail.__head
        if not isnull(tail.__tail):
            self.__tail = tail.__tail + current.__tail
        else:
            self.__tail = current.__tail
        return head
    def clear(self):
        self.__head = Null()
        self.__tail = Null()
    def isempty(self):
        return isnull(self.__head)
    def copy(self):
        new_list = List()
        new_list.__head = self.__head
        new_list.__tail = self.__tail
        return new_list
    def eval(self):
        return self

class Lambda(Base):
    _type ='lambda'
    def __init__(self, params, body):
        self.params = params
        self.body = body
    def __repr__(self):
        return f'[lambda: {self.params}: {self.body}]'
    def eval(self):
        return self

def isnull(value):
    return isinstance(value, Null)

def islambda(value):
    return isinstance(value.eval(), Lambda)

def isvariable(value):
    return isinstance(value, Variable)

def is_(value):
    if value: return True
    else: return False

def ttype(value):
    if isinstance(value, bool):
        return Bool(value)
    if isinstance(value, int) or isinstance(value, float):
        return Number(value)
    if isinstance(value, str):
        return String(value)
    if value is None:
        return Null()
    return value

