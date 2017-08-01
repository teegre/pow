# typedef.py: [PowerText type definition]
# _*_ coding:utf8 _*_
from time import sleep

class Base:
    def eval(self):
        raise NotImplementedError
    def powtype(self):
        return self.__type

class Number(Base):
    __type = 'number'
    def __init__(self, value):
        self.__value = value
    def __repr__(self):
        return str(self.__value)
    def __str__(self):
        return str(self.__value)
    def eval(self):
        return self.__value

class String(Base):
    __type = 'string'
    def __init__(self, value):
        self.__value = value
    def __repr__(self):
       return f'"{self.value}"'
    def __str__(self):
        return self.__value
    def eval(self):
        return self.__value

class Bool(Base):
    __type = 'bool'
    def __init__(self, value):
        if value != 0: self.__value = True
        else: self.__value = False
    def __repr__(self):
        return 'bool: ' + str(self.__value).lower()
    def __str__(self):
        return str(self.__value).lower()
    def eval(self):
        return self.__value

class Null(Base):
    __type = 'null'
    def __init__(self):
        self.__value = '\0'
    def __getitem__(self, index):
        return self
    def __setitem__(self, index, value):
        return self
    def __repr__(self):
        return 'null'
    def __str__(self):
        return self.__value
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
    if s.isempty(): return t
    return List(s.head(), addlist(s.tail(), t))

class List(Base):
    """List type from scratch"""
    __type = 'list'
    def __init__(self, head=Null(), tail=Null()):
        assert isnull(tail) or isinstance(tail, List)
        self.__head = head
        self.__tail = tail
    def __repr__(self):
        return f'( {listrepr(self)} )'
    def __getitem__(self, start, end=Null()):
        if isnull(end):
            if start == 0: return self.__head
            return self.__tail[start-1]
        if start == 0: return self.__head + self.__tail[:end]
        return self.__tail[start:end-1]
    def __setitem__(self, index, value):
        if index == 0: self.__head = value
        else: self.__tail[index-1] = value
        return value
    def __len__(self):
        return 1 + len(self.__tail)
    def __add__(self, other):
        return addlist(self, other)
    def __eq__(self, other):
        if not isinstance(other, List): return False
        return self.__head == other.__head and self.__tail == other.__tail
    def __ne__(self, other):
        if not isinstance(other, List): return True
        return self.__head != other.__head and self.__tail != other.__tail
    def powtype(self):
        return String('list')
    def head(self):
        """first element of the list"""
        return self.__head
    def tail(self):
        """all elements of the list except first one"""
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
    def isempty(self):
        if isnull(self.__head): return True
        else: return False
    def copy(self):
        new_list = List()
        new_list.__head = self.__head
        new_list.__tail = self.__tail
        return new_list
    def eval(self):
        return self

class Lambda(Base):
    __type ='lambda'
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

def ttype(value):
    if isinstance(value, int) or isinstance(value, float):
        return Number(value)
    if isinstance(value, str):
        return String(value)
    if isinstance(value, bool):
        return Bool(value)
    if value is None:
        return Null()
    return value

