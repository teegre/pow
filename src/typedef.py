# typedef.py: [PowerText type definition]
# _*_ coding:utf8 _*_
from time import sleep

class Base:
    def eval(self):
        raise NotImplementedError

class Number(Base):
    def __init__(self, value):
        self.value = value
    def __len__(self):
        return len(str(self.value))
    def __repr__(self):
        return f'{self.value}'
    def powtype(self):
        return 'number'
    def tostr(self):
        return str(self.value)
    def eval(self):
        return self.value

class String(Base):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
       return f'"{self.value}"'
    def __add__(self, other):
        try: return self.value + other.value
        except: return self.value + other
    def __len__(self):
        return len(self.value)
    def __iter__(self):
        return iter(self.value)
    def __getitem__(self, index):
        return self.value[index]
    def __setitem__(self, index, value):
        l = [c for c in self.value]
        l[index] = value
        self.value = ''.join(l)
        return value
    def powtype(self):
        return 'string'
    def tonum(self):
        try: num = int(self.value)
        except:
            try: num = float(self.value)
            except:
                print(f'*** unable to convert "{self.value}" to a number.')
                #return self.value
        return Number(num)
    def eval(self):
        return self

class Bool(Base):
    def __init__(self, value):
        if value != 0: self.value = TRUE()
        else: self.value = FALSE()
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return 'bool: ' + repr(self.value)
    def __eq__(self, other):
        return self.value == other
    def __ne__(self, other):
        return self.value != other
    def __gt__(self, other):
        return self.value > other
    def __ge__(self, other):
        return self.value >= other
    def __lt__(self, other):
        return self.value < other
    def __le__(self, other):
        return self.value <= other
    def powtype(self):
        return 'bool'
    def eval(self):
        return self.value.eval()

class TRUE(Bool):
    def __init__(self):
        self.value = 1
    def __repr__(self):
        return 'true'
    def __str__(self):
        return 'true'
    def eval(self):
        return self

class FALSE(Bool):
    def __init__(self):
        self.value = 0
    def __repr__(self):
        return 'false'
    def __str__(self):
        return 'false'
    def eval(self):
        return self

class Null(Base):
    def __init__(self):
        self.value = '\0'
    def __getitem__(self, index):
        return self
    def __setitem__(self, index, value):
        return self
    def __repr__(self):
        return 'null'
    def __str__(self):
        return '\0'
    def __len__(self):
        return 0
    def __eq__(self, other):
        return Bool(isinstance(other, Null))
    def __ne__(self, other):
        return Bool(not isinstance(other, Null))
    def __gt__(self, other):
        return Bool(0)
    def __ge__(self, other):
        if isinstance(other, Null): return Bool(1)
        else: return Bool(0)
    def __lt__(self, other):
        return Bool(0)
    def __le__(self, other):
        if isinstance(other, Null): return Bool(1)
        else: return Bool(0)
    def powtype(self):
        return 'null'
    def eval(self):
        return self

def listrepr(s):
    tail = ''
    if not isnull(s.tail()):
        tail = ', ' + listrepr(s.tail())
    return f'{s.head()}{tail}'

def addlist(s, t):
    if isnull(s): return t
    if s.isempty(): return t
    return List(s.head(), addlist(s.tail(), t))

class List(Base):
    """List type from scratch"""
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
        if not isinstance(other, List): return Bool(0)
        return Bool(self.__head == other.__head and self.__tail == other.__tail)
    def __ne__(self, other):
        if not isinstance(other, List): return Bool(1)
        return Bool(self.__head != other.__head and self.__tail != other.__tail)
    def powtype(self):
        return 'list'
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
        if isnull(self.head()): return True
        else: return False
    def copy(self):
        new_list = List()
        new_list.__head = self.__head
        new_list.__tail = self.__tail
        return new_list
    def eval(self):
        return self

#def strrepr(s):
#    tail = ''
#    if not isnull(s.tail()):
#        tail = listrepr(s.tail())
#    return f'{s.head()}{tail}'
#
#class String(List):
#    def powtype(self):
#        return 'string'
#    def __repr__(self):
#        return f'"{strrepr(self)}"'
#    def __str__(self):
#        return f'{strrepr(self)}'
#    def eval(self):
#        return self

class Lambda(Base):
    def __init__(self, params, body):
        self.params = params
        self.body = body
    def powtype(self):
        return 'lambda'
    def __repr__(self):
        return f'[lambda: {self.params}: {self.body}]'
    def eval(self):
        return self

def isnull(value):
    return isinstance(value, Null)

def istrue(value):
    value = Bool(value)
    return isinstance(value.value, TRUE)

def isfalse(value):
    value = Bool(value)
    return isinstance(value.value, FALSE)

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

