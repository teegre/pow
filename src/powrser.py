import ply.yacc as yacc
from powlexer import tokens
import powast
from exceptions import *

precedence = (
        ('right', 'UMINUS'),
)

def p_statements(p):
    """statements : statement
                  | statements statement"""
    if len(p) == 2:
        p[0] = powast.StatementList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]

def p_statement(p):
    """statement : expr"""
    p[0] = powast.ttype(p[1])

def p_sequence(p):
    """sequence : element
                | sequence element"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_element(p):
    """element : expr"""
    p[0] = [p[1]]

def p_id_sequence(p):
    """ id_sequence : id_element
                    | id_sequence id_element"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_id_element(p):
    """id_element : ID"""
    p[0] = [p[1]]

def p_expr(p):
    """expr : LBRACKET command RBRACKET
            | STRING
            | NUMBER
            | BOOL
            | NULL
            | variable
            | list_expr
            | lambda_expr
            | if_statement
            | while_statement
            | exit_statement
            | for_statement"""
    if len(p) == 4:
        p[0] = powast.ttype(p[2])
    else:
        p[0] = powast.ttype(p[1])

def p_variable(p):
    """variable : ID
                | LPAREN ID COLUMN expr RPAREN"""
    if len(p) == 2:
        p[0] = powast.Variable(p[1])
    else:
        p[0] = powast.Get(powast.Variable(p[2]), p[4])

def p_list_expr(p):
    """list_expr : LPAREN RPAREN
                 | LPAREN sequence RPAREN"""
    if len(p) == 3:
        p[0] = powast.List()
    else:
        p[0] = powast.MakeList(p[2])

def p_lambda_expr(p):
    """lambda_expr : AT variable"""
    p[0] = powast.LambdaCall(p[2], [])

def p_if_statement(p):
    """if_statement : LBRACKET QUESTION expr COLUMN statements RBRACKET
                    | LBRACKET QUESTION expr COLUMN statements SEMI statements RBRACKET"""
    if len(p) == 7:
        p[0] = powast.If(p[3], p[5], powast.Null())
    else:
        p[0] = powast.If(p[3], p[5], p[7])

def p_while_statement(p):
    """while_statement : LBRACKET WHILE expr COLUMN statements RBRACKET"""
    p[0] = powast.While(p[3], p[5])

def p_exit_statement(p):
    """exit_statement : LBRACKET EXIT RBRACKET
                      | LBRACKET EXIT expr RBRACKET"""
    if len(p) == 4: p[0] = powast.Exit(powast.Null())
    else: p[0] = powast.Exit(p[3])

def p_for_statement(p):
    """for_statement : LBRACKET FOR LBRACKET ID expr expr RBRACKET COLUMN statements RBRACKET
                     | LBRACKET FOR LBRACKET ID expr expr expr RBRACKET COLUMN statements RBRACKET"""
    if len(p) == 11:
        p[0] = powast.For(p[4], p[5], p[6], powast.Number(1), p[9])
    else:
        p[0] = powast.For(p[4], p[5], p[6], p[7], p[10])

def p_expr_uminus(p):
    """expr : MINUS expr %prec UMINUS"""
    p[0] = powast.Negative(p[2])

def p_command_echo(p):
    """command : ECHO
               | ECHO sequence"""
    if len(p) == 2:
        p[0] = powast.Echo()
    else:
        p[0] = powast.Echo(p[2])

def p_command_binop(p):
    """command : PLUS  expr expr
               | MINUS expr expr
               | MUL   expr expr
               | DIV   expr expr
               | IDIV  expr expr
               | MOD   expr expr
               | POW   expr expr
               | EQ    expr expr
               | NE    expr expr
               | LT    expr expr
               | LE    expr expr
               | GT    expr expr
               | GE    expr expr"""
    p[0] = powast.BinOp(p[1], p[2], p[3])

def p_command_incdec(p):
    """command : INC ID
               | DEC ID"""
    p[0] = powast.IncDec(p[1], p[2])

def p_command_pow2(p):
    """command : POW2 expr"""
    p[0] = powast.Pow2(p[2])

def p_command_boolop(p):
    """command : AND expr expr
               | OR  expr expr
               | XOR expr expr
               | NOT expr"""
    if len(p) == 4:
        if    p[1] == 'and': p[0] = powast.And(p[2], p[3])
        elif  p[1] == 'or': p[0] = powast.Or(p[2], p[3])
        else: p[0] = powast.XOr(p[2], p[3])
    else:
        p[0] = powast.Not(p[2])

def p_command_listcmd(p):
    """command : HEAD expr
               | TAIL expr
               | LAST expr
               | LEN  expr
               | MAP expr expr
               | FILTER expr expr"""
    if    p[1] == 'head'  : p[0] = powast.Head(p[2])
    elif  p[1] == 'tail'  : p[0] = powast.Tail(p[2])
    elif  p[1] == 'last'  : p[0] = powast.Last(p[2])
    elif  p[1] == 'map'   : p[0] = powast.Map(p[2], p[3])
    elif  p[1] == 'filter': p[0] = powast.Filter(p[2], p[3])
    else: p[0] = powast.Len(p[2])


def p_command_set(p):
    """command : SET ID expr
               | SET LPAREN ID COLUMN expr RPAREN expr"""
    if len(p) == 4:
        p[0] = powast.Set(p[2], p[3])
    else:
        p[0] = powast.Set(p[3], p[7], p[5])

def p_command_push(p):
    """command : PUSH ID sequence"""
    p[0] = powast.Push(powast.Variable(p[2]), p[3])

def p_command_def(p):
    """command : DEF ID LBRACKET RBRACKET COLUMN statements
               | DEF ID LBRACKET id_sequence RBRACKET COLUMN statements"""
    if len(p) == 7:
        p[0] = powast.Def(p[2], [], p[6])
    else:
        p[0] = powast.Def(p[2], p[4], p[7])

def p_command_call(p):
    """command : ID
               | ID sequence"""
    if len(p) == 2:
        p[0] = powast.FunctionCall(p[1], [])
    else:
        p[0] = powast.FunctionCall(p[1], p[2])

def p_command_lambda(p):
    """command : LAMBDA LBRACKET id_sequence RBRACKET COLUMN expr"""
    p[0] = powast.Lambda(p[3], p[6])

def p_command_lambdacall(p):
    """command : AT ID sequence"""
    p[0] = powast.LambdaCall(powast.Variable(p[2]), p[3])

def p_command_del(p):
    """command : DEL ID"""
    p[0] = powast.Del(p[2])

def p_command_rnd(p):
    """command : RND"""
    p[0] = powast.Rnd()

def p_command_time(p):
    """command : TIME"""
    p[0] = powast.Time()

def p_command_pause(p):
    """command : PAUSE expr"""
    p[0] = powast.Pause(p[2])

def p_command_getcur(p):
    """command : GETCUR"""
    p[0] = powast.GetCursor()

def p_command_scrsize(p):
    """command : SCRSIZE"""
    p[0] = powast.ScreenSize()

def p_command_uses(p):
    """command : USES ID"""
    parser = yacc.yacc()
    p[0] = powast.Uses(p[2], parser)

def p_error(p):
    if p:
        raise PowSyntaxError(f'*** syntax error: < {p.value} >\n*** line: {p.lineno}\n*** position: {p.lexpos+1}')
    else:
        print('*** unexpected end of input')

parser = yacc.yacc()
try: parser.parse('[uses std]').eval()
except: print('*** std module error', end='')
