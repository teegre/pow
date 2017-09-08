# lexer.py: [PowerText] language lexer.
# _*_ coding:utf8 _*_

import ply.lex as lex
from typedef import *
from exceptions import *

# Reserved words.
reserved = {
        'bool'    : 'TYPE_BOOL',
        'int'     : 'TYPE_INT',
        'real'    : 'TYPE_REAL',
        'frac'    : 'TYPE_FRAC',
        'string'  : 'TYPE_STR',
        'list'    : 'TYPE_LIST',
        'echo'    : 'ECHO',     #OK print function
        'read'    : 'READ',     #   user input
        'expect'  : 'EXPECT',   #   check type
        'set'     : 'SET',      #OK variable assignation
        'setg'    : 'SETG',     #   global variable assignment
        'del'     : 'DEL',      #OK variable / function deletion
        'for'     : 'FOR',      #OK for loop
        'while'   : 'WHILE',    #OK while statement
        'exit'    : 'EXIT',     #OK exit statement
        'skip'    : 'SKIP',     #OK skip statement
        'def'     : 'DEF',      #OK function definition
        'lambda'  : 'LAMBDA',   #OK lambda expression
#        'defn'    : 'DEFN',     #   namespace definition
        'len'     : 'LEN',      #OK
        'not'     : 'NOT',      #OK
        'and'     : 'AND',      #OK
        'or'      : 'OR',       #OK
        'xor'     : 'XOR',
        'rnd'     : 'RND',      #OK random number (0...1)
        'head'    : 'HEAD',     #OK first element of a list
        'tail'    : 'TAIL',     #OK all elements after the first one
        'push'    : 'PUSH',     #OK add item(s) to a list
        'pop'     : 'POP',      #OK remove an item from a list
        'clear'   : 'CLEAR',    #OK clear a list
        'map'     : 'MAP',      #
        'filter'  : 'FILTER',   #
        'type'    : 'TYPE',     #
        'tostr'   : 'TOSTR',    #   convert a number to a string
        'tonum'   : 'TONUM',    #   convert a string to a number
        'tofrac'  : 'TOFRAC',   #   convert a string to a fraction
        'cal'     : 'CAL',      #   evaluate fraction
        'uses'    : 'USES',     #   module import
        'char'    : 'CHAR',     #
        'ord'     : 'ORD',      #
        'getcur'  : 'GETCUR',   #   cursor position
        'scrsize' : 'SCRSIZE',  #   screen size
        'time'    : 'TIME',    #OK
        'pause'   : 'PAUSE',   #OK  pause program execution
}

# List of token names.
tokens = [
            'NULL', 'INT', 'REAL', 'FRAC', 'BOOL', 'STRING',
            'EQ', 'NE', 'GT', 'GE', 'LT', 'LE',
            'PLUS', 'MINUS', 'MUL', 'DIV', 'IDIV', 'MOD', 'POW', 'POW2',
            'LSHIFT', 'RSHIFT', 'INC', 'DEC', 'PLUSONE', 'MINUSONE',
            'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'AT', 'QUESTION',
            'COLUMN', 'SEMI', 'IS',
            'ID',
] + list(reserved.values())

t_PLUS     = r'\+'
t_POW      = r'\*\*\*'
t_POW2     = r'\*\*'
t_MUL      = r'\*'
t_IDIV     = r'//'
t_DIV      = r'/'
t_EQ       = '='
t_NE       = '!='
t_GE       = '>='
t_LE       = '<='
t_LSHIFT   = '<<'
t_RSHIFT   = '>>'
t_GT       = '>'
t_LT       = '<'
t_MOD      = '%'
t_INC      = r'\+\+'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_AT       = r'@'
t_IS       = r'\?\?'
t_QUESTION = r'\?'
t_COLUMN   = r'\:'
t_SEMI     = r';'

t_ignore   = ' \t'

def t_PLUSONE(t):
    r'1\+'
    return t

def t_MINUSONE(t):
    r'1-'
    return t

def t_BOOL(t):
    r'\btrue\b|\bfalse\b'
    if t.value == 'true':
        t.value = Bool(1)
    elif t.value == 'false':
        t.value = Bool(0)
    return t

def t_NULL(t):
    r'\bnull\b'
    t.value = Null()
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    # issue with escaped double quote in double-quoted strings.
    # workaround: enabling single-quoted strings...
    r'\".*?\"|\'.*?\''
    t.value = bytes(t.value[1:-1], 'latin-1').decode('unicode-escape')
    return t

def t_DEC(t):
    r'--'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_ID(t):
    r'[a-zA-Z\-_][a-zA-Z\-_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'(?:;;.*|\#.*)'
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_eof(t):
    t.lexer.lineno = 1
    return None

def t_error(t):
    raise IllegalCharacter(f'*** illegal character < {t.value[0]} >\n*** line: {t.lexer.lineno}\n*** position: {t.lexer.lexpos+1}')

#lexer = lex.lex(optimize=1)
lexer = lex.lex()
