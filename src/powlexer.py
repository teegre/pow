# lexer.py: [PowerText] language lexer.
# _*_ coding:utf8 _*_

import ply.lex as lex
from typedef import Null, List, Bool, TRUE, FALSE
from exceptions import *
# Reserved words.
reserved = {
        'echo'   : 'ECHO',     #OK print function
#        'input'  : 'INPUT',    #   user input
        'set'    : 'SET',      #OK variable assignation
        'del'    : 'DEL',      #OK variable / function deletion
        'for'    : 'FOR',      #    for loop
        'while'  : 'WHILE',    #OK while statement
        'exit'   : 'EXIT',     #OK break statement
        'def'    : 'DEF',      #OK function definition
        'lambda' : 'LAMBDA',   #   lambda expression
#        'defn'   : 'DEFN',     #   namespace definition
        'len'    : 'LEN',      #OK
        'not'    : 'NOT',      #OK
        'and'    : 'AND',      #OK
        'or'     : 'OR',       #OK
        'xor'    : 'XOR',
        'rnd'    : 'RND',      #OK random number (0...1)
        'head'   : 'HEAD',     #OK first element of a list
        'tail'   : 'TAIL',     #OK all elements after the first one
        'last'   : 'LAST',     #OK last element (null terminated)
        'push'   : 'PUSH',     #OK add item(s) in a list
#        'pop'    : 'POP',      #NOT OK remove an item from a list
        'map'    : 'MAP',      #
        'filter' : 'FILTER',   #
#        'sort'   : 'SORT',     #OK [useless]
#        'rndl'   : 'RNDL',     #OK [useless]
#        'reverse': 'REVERSE',  #OK [useless]
#        'it'     : 'IT',       #NOT OK iterate through a list
#        'tolist' : 'TOLIST',   #OK convert a string to a list
#        'tostr'  : 'TOSTR',    #OK convert a list or a string to a list
#        'tonum'  : 'TONUM',    #OK convert a string to a number
        'uses'    : 'USES',     #   module import
        'getcur'  : 'GETCUR',   #   cursor position
        'scrsize' : 'SCRSIZE',  #   screen size
        'time'    : 'TIME',     #OK
        'pause'   : 'PAUSE',    #OK pause program execution
}

# List of token names.
tokens = [
            'NULL', 'NUMBER', 'BOOL', 'STRING',
            'EQ', 'NE', 'GT', 'GE', 'LT', 'LE',
            'PLUS', 'MINUS', 'MUL', 'DIV', 'IDIV', 'MOD', 'POW', 'POW2',
            'INC', 'DEC',
            'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'AT', 'QUESTION',
            'COLUMN', 'SEMI',
            'ID',
            #'NEWLINE',
] + list(reserved.values())

t_PLUS     = r'\+'
t_MINUS    = '-'
t_POW      = r'\*\*\*'
t_POW2     = r'\*\*'
t_MUL      = r'\*'
t_IDIV     = r'//'
t_DIV      = r'/'
t_EQ       = '='
t_NE       = '!='
t_GE       = '>='
t_LE       = '<='
t_GT       = '>'
t_LT       = '<'
t_MOD      = '%'
t_INC      = r'\+\+'
t_DEC      = '--'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_AT       = r'@'
t_QUESTION = r'\?'
t_COLUMN   = r'\:'
t_SEMI     = r';'

t_ignore   = ' \t'

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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d*\.?\d+'
    try: t.value = int(t.value)
    except:
        try: t.value = float(t.value)
        except: pass
    return t

def t_STRING(t):
    # issue with escaped double quote in double-quoted strings.
    # workaround: enabling single-quoted strings...
    r'\".*?\"|\'.*?\''
    t.value = bytes(t.value[1:-1], 'utf-8').decode('unicode_escape')
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
