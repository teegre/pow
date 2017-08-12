
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightUMINUSNULL NUMBER BOOL STRING EQ NE GT GE LT LE PLUS MINUS MUL DIV IDIV MOD POW POW2 INC DEC PLUSONE MINUSONE LPAREN RPAREN LBRACKET RBRACKET AT QUESTION COLUMN SEMI IS ID TYPE_BOOL TYPE_NUM TYPE_STR TYPE_LIST ECHO READ EXPECT SET SETG DEL FOR WHILE EXIT SKIP DEF LAMBDA LEN NOT AND OR XOR RND HEAD TAIL PUSH POP MAP FILTER TYPE TOSTR TONUM USES CHAR ORD GETCUR SCRSIZE TIME PAUSEstatements : statement\n                  | statements statementstatement : exprsequence : element\n                | sequence elementelement : expr id_sequence : id_element\n                    | id_sequence id_elementid_element : IDexpr : LBRACKET command RBRACKET\n            | STRING\n            | NUMBER\n            | BOOL\n            | NULL\n            | pow_type\n            | variable\n            | list_expr\n            | list_access\n            | lambda_expr\n            | if_statement\n            | while_statement\n            | exit_statement\n            | for_statementpow_type : TYPE_BOOL\n                | TYPE_NUM\n                | TYPE_STR\n                | TYPE_LISTvariable : IDlist_access : LPAREN expr COLUMN expr RPARENlist_expr : LPAREN RPAREN\n                 | LPAREN sequence RPARENlambda_expr : AT variableif_statement : LBRACKET QUESTION expr COLUMN statements RBRACKET\n                    | LBRACKET QUESTION expr COLUMN statements SEMI statements RBRACKETwhile_statement : LBRACKET WHILE expr COLUMN statements RBRACKETexit_statement : LBRACKET EXIT RBRACKET\n                      | LBRACKET EXIT expr RBRACKETcommand : SKIPfor_statement : LBRACKET FOR ID expr expr COLUMN statements RBRACKET\n                     | LBRACKET FOR ID expr expr expr COLUMN statements RBRACKETexpr : MINUS expr %prec UMINUScommand : IS exprcommand : ECHO\n               | ECHO sequencecommand : READ\n               | READ sequencecommand : EXPECT pow_type exprcommand : PLUS  expr expr\n               | MINUS expr expr\n               | MUL   expr expr\n               | DIV   expr expr\n               | IDIV  expr expr\n               | MOD   expr expr\n               | POW   expr expr\n               | EQ    expr expr\n               | NE    expr expr\n               | LT    expr expr\n               | LE    expr expr\n               | GT    expr expr\n               | GE    expr exprcommand : PLUSONE exprcommand : MINUSONE exprcommand : INC ID\n               | DEC IDcommand : POW2 exprcommand : AND expr expr\n               | OR  expr expr\n               | XOR expr expr\n               | NOT exprcommand : HEAD expr\n               | TAIL expr\n               | LEN  expr\n               | MAP expr expr\n               | FILTER expr exprcommand : TYPE exprcommand : TOSTR exprcommand : TONUM exprcommand : CHAR exprcommand : ORD exprcommand : SET ID expr\n               | SET LPAREN ID COLUMN expr RPAREN exprcommand : SETG ID expr\n               | SETG LPAREN ID COLUMN expr RPAREN exprcommand : PUSH ID sequencecommand : POP ID\n               | POP ID exprcommand : DEF ID LBRACKET RBRACKET COLUMN statements\n               | DEF ID LBRACKET id_sequence RBRACKET COLUMN statementscommand : ID\n               | ID sequencecommand : LAMBDA LBRACKET RBRACKET COLUMN expr\n               | LAMBDA LBRACKET id_sequence RBRACKET COLUMN exprcommand : AT ID\n               | AT ID sequencecommand : DEL IDcommand : RNDcommand : TIMEcommand : PAUSE exprcommand : GETCURcommand : SCRSIZEcommand : USES ID'
    
_lr_action_items = {'LBRACKET':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,75,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,140,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[4,4,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,4,-24,-25,-26,-27,-28,4,-2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,141,4,-41,-30,4,-6,-4,-32,-10,-36,4,4,-6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,178,4,-31,-5,4,4,4,-37,4,4,4,4,4,4,4,4,4,-29,-33,4,-35,4,4,4,4,4,4,4,4,4,4,-34,4,-39,4,-40,]),'STRING':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[5,5,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,5,-24,-25,-26,-27,-28,5,-2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-41,-30,5,-6,-4,-32,-10,-36,5,5,-6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-31,-5,5,5,5,-37,5,5,5,5,5,5,5,5,5,-29,-33,5,-35,5,5,5,5,5,5,5,5,5,5,-34,5,-39,5,-40,]),'NUMBER':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[6,6,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,6,-24,-25,-26,-27,-28,6,-2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-41,-30,6,-6,-4,-32,-10,-36,6,6,-6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-31,-5,6,6,6,-37,6,6,6,6,6,6,6,6,6,-29,-33,6,-35,6,6,6,6,6,6,6,6,6,6,-34,6,-39,6,-40,]),'BOOL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[7,7,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,7,-24,-25,-26,-27,-28,7,-2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-41,-30,7,-6,-4,-32,-10,-36,7,7,-6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-31,-5,7,7,7,-37,7,7,7,7,7,7,7,7,7,-29,-33,7,-35,7,7,7,7,7,7,7,7,7,7,-34,7,-39,7,-40,]),'NULL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[8,8,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,8,-24,-25,-26,-27,-28,8,-2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-41,-30,8,-6,-4,-32,-10,-36,8,8,-6,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-31,-5,8,8,8,-37,8,8,8,8,8,8,8,8,8,-29,-33,8,-35,8,8,8,8,8,8,8,8,8,8,-34,8,-39,8,-40,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[18,18,-1,-3,39,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,18,-24,-25,-26,-27,-28,18,-2,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-41,-30,18,-6,-4,-32,-10,-36,18,18,-6,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-31,-5,18,18,18,-37,18,18,18,18,18,18,18,18,18,-29,-33,18,-35,18,18,18,18,18,18,18,18,18,18,-34,18,-39,18,-40,]),'TYPE_BOOL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[19,19,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,19,-24,-25,-26,-27,-28,19,-2,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-41,-30,19,-6,-4,-32,-10,-36,19,19,-6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-31,-5,19,19,19,-37,19,19,19,19,19,19,19,19,19,-29,-33,19,-35,19,19,19,19,19,19,19,19,19,19,-34,19,-39,19,-40,]),'TYPE_NUM':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[20,20,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,20,-24,-25,-26,-27,-28,20,-2,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-41,-30,20,-6,-4,-32,-10,-36,20,20,-6,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-31,-5,20,20,20,-37,20,20,20,20,20,20,20,20,20,-29,-33,20,-35,20,20,20,20,20,20,20,20,20,20,-34,20,-39,20,-40,]),'TYPE_STR':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[21,21,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,21,-24,-25,-26,-27,-28,21,-2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-41,-30,21,-6,-4,-32,-10,-36,21,21,-6,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-31,-5,21,21,21,-37,21,21,21,21,21,21,21,21,21,-29,-33,21,-35,21,21,21,21,21,21,21,21,21,21,-34,21,-39,21,-40,]),'TYPE_LIST':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[22,22,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,22,-24,-25,-26,-27,-28,22,-2,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-41,-30,22,-6,-4,-32,-10,-36,22,22,-6,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-31,-5,22,22,22,-37,22,22,22,22,22,22,22,22,22,-29,-33,22,-35,22,22,22,22,22,22,22,22,22,22,-34,22,-39,22,-40,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,83,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,135,136,137,138,139,141,142,146,147,148,149,150,151,152,176,178,180,181,182,183,185,186,187,188,189,191,192,194,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[23,23,-1,-3,32,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,23,-24,-25,-26,-27,-28,23,23,-2,23,23,23,95,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,117,118,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,134,136,138,139,140,142,143,23,145,-41,-30,23,-6,-4,-32,-10,-36,23,23,-6,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,173,23,175,23,23,182,23,-31,-5,23,23,23,-37,23,23,182,182,-7,-9,23,23,23,23,23,23,182,23,-8,-29,-33,23,-35,23,23,23,23,23,23,23,23,23,23,-34,23,-39,23,-40,]),'LPAREN':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[24,24,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,24,-24,-25,-26,-27,-28,24,-2,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,135,137,24,-41,-30,24,-6,-4,-32,-10,-36,24,24,-6,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-31,-5,24,24,24,-37,24,24,24,24,24,24,24,24,24,-29,-33,24,-35,24,24,24,24,24,24,24,24,24,24,-34,24,-39,24,-40,]),'AT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,84,85,86,87,88,89,90,93,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,146,147,148,149,150,151,152,176,183,185,186,187,188,189,192,195,196,197,198,200,203,206,207,208,209,210,211,212,213,215,216,217,220,221,],[25,25,-1,-3,76,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,25,-24,-25,-26,-27,-28,25,-2,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-41,-30,25,-6,-4,-32,-10,-36,25,25,-6,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-31,-5,25,25,25,-37,25,25,25,25,25,25,25,25,25,-29,-33,25,-35,25,25,25,25,25,25,25,25,25,25,-34,25,-39,25,-40,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,84,85,89,90,93,146,151,195,196,198,215,217,221,],[0,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,-41,-30,-32,-10,-36,-31,-37,-29,-33,-35,-34,-39,-40,]),'RBRACKET':([2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,27,30,32,33,35,36,78,79,81,82,84,85,88,89,90,93,94,96,97,98,99,100,115,116,117,118,119,123,124,125,126,129,130,131,132,133,139,141,142,143,144,145,146,147,151,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,174,176,177,178,180,181,182,183,185,186,191,194,195,196,198,205,207,209,212,214,215,216,217,218,219,220,221,],[-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,90,93,-89,-38,-43,-45,-96,-97,-99,-100,-41,-30,-4,-32,-10,-36,151,-90,-6,-42,-44,-46,-61,-62,-63,-64,-65,-69,-70,-71,-72,-75,-76,-77,-78,-79,-85,179,-93,-95,-98,-101,-31,-5,-37,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-66,-67,-68,-73,-74,-80,-82,-84,-86,190,193,-7,-9,-94,196,198,204,-8,-29,-33,-35,-91,215,217,-87,-92,-34,221,-39,-81,-83,-88,-40,]),'SEMI':([2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,84,85,89,90,93,146,151,185,195,196,198,215,217,221,],[-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,-41,-30,-32,-10,-36,-31,-37,197,-29,-33,-35,-34,-39,-40,]),'QUESTION':([4,],[28,]),'WHILE':([4,],[29,]),'EXIT':([4,],[30,]),'FOR':([4,],[31,]),'SKIP':([4,],[33,]),'IS':([4,],[34,]),'ECHO':([4,],[35,]),'READ':([4,],[36,]),'EXPECT':([4,],[37,]),'PLUS':([4,],[38,]),'MUL':([4,],[40,]),'DIV':([4,],[41,]),'IDIV':([4,],[42,]),'MOD':([4,],[43,]),'POW':([4,],[44,]),'EQ':([4,],[45,]),'NE':([4,],[46,]),'LT':([4,],[47,]),'LE':([4,],[48,]),'GT':([4,],[49,]),'GE':([4,],[50,]),'PLUSONE':([4,],[51,]),'MINUSONE':([4,],[52,]),'INC':([4,],[53,]),'DEC':([4,],[54,]),'POW2':([4,],[55,]),'AND':([4,],[56,]),'OR':([4,],[57,]),'XOR':([4,],[58,]),'NOT':([4,],[59,]),'HEAD':([4,],[60,]),'TAIL':([4,],[61,]),'LEN':([4,],[62,]),'MAP':([4,],[63,]),'FILTER':([4,],[64,]),'TYPE':([4,],[65,]),'TOSTR':([4,],[66,]),'TONUM':([4,],[67,]),'CHAR':([4,],[68,]),'ORD':([4,],[69,]),'SET':([4,],[70,]),'SETG':([4,],[71,]),'PUSH':([4,],[72,]),'POP':([4,],[73,]),'DEF':([4,],[74,]),'LAMBDA':([4,],[75,]),'DEL':([4,],[77,]),'RND':([4,],[78,]),'TIME':([4,],[79,]),'PAUSE':([4,],[80,]),'GETCUR':([4,],[81,]),'SCRSIZE':([4,],[82,]),'USES':([4,],[83,]),'COLUMN':([5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,84,85,87,89,90,91,92,93,146,151,173,175,179,187,190,193,195,196,198,199,204,215,217,221,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-41,-30,148,-32,-10,149,150,-36,-31,-37,188,189,192,200,203,206,-29,-33,-35,208,213,-34,-39,-40,]),'RPAREN':([5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,84,85,86,87,88,89,90,93,97,146,147,151,184,195,196,198,201,202,215,217,221,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,85,-41,-30,146,-6,-4,-32,-10,-36,-6,-31,-5,-37,195,-29,-33,-35,210,211,-34,-39,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,149,150,197,200,203,208,213,],[1,185,186,207,209,212,216,220,]),'statement':([0,1,149,150,185,186,197,200,203,207,208,209,212,213,216,220,],[2,26,2,2,26,26,2,2,2,26,2,26,26,2,26,26,]),'expr':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[3,3,84,87,91,92,94,97,98,97,97,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,144,97,152,97,97,97,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,174,97,177,97,184,3,3,187,97,97,3,3,199,201,202,205,3,3,3,214,3,3,3,218,219,3,3,3,3,]),'pow_type':([0,1,18,24,28,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[9,9,9,9,9,9,9,9,9,9,9,101,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'variable':([0,1,18,24,25,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[10,10,10,10,89,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'list_expr':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'list_access':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'lambda_expr':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'if_statement':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'while_statement':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'exit_statement':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'for_statement':([0,1,18,24,28,29,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,86,95,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,120,121,122,127,128,134,136,138,139,142,148,149,150,152,176,183,185,186,187,188,189,192,197,200,203,206,207,208,209,210,211,212,213,216,220,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'command':([4,],[27,]),'sequence':([24,32,35,36,138,142,],[86,96,99,100,176,183,]),'element':([24,32,35,36,86,96,99,100,138,142,176,183,],[88,88,88,88,147,147,147,147,88,88,147,147,]),'id_sequence':([141,178,],[180,191,]),'id_element':([141,178,180,191,],[181,181,194,194,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','powrser.py',11),
  ('statements -> statements statement','statements',2,'p_statements','powrser.py',12),
  ('statement -> expr','statement',1,'p_statement','powrser.py',20),
  ('sequence -> element','sequence',1,'p_sequence','powrser.py',24),
  ('sequence -> sequence element','sequence',2,'p_sequence','powrser.py',25),
  ('element -> expr','element',1,'p_element','powrser.py',32),
  ('id_sequence -> id_element','id_sequence',1,'p_id_sequence','powrser.py',36),
  ('id_sequence -> id_sequence id_element','id_sequence',2,'p_id_sequence','powrser.py',37),
  ('id_element -> ID','id_element',1,'p_id_element','powrser.py',44),
  ('expr -> LBRACKET command RBRACKET','expr',3,'p_expr','powrser.py',48),
  ('expr -> STRING','expr',1,'p_expr','powrser.py',49),
  ('expr -> NUMBER','expr',1,'p_expr','powrser.py',50),
  ('expr -> BOOL','expr',1,'p_expr','powrser.py',51),
  ('expr -> NULL','expr',1,'p_expr','powrser.py',52),
  ('expr -> pow_type','expr',1,'p_expr','powrser.py',53),
  ('expr -> variable','expr',1,'p_expr','powrser.py',54),
  ('expr -> list_expr','expr',1,'p_expr','powrser.py',55),
  ('expr -> list_access','expr',1,'p_expr','powrser.py',56),
  ('expr -> lambda_expr','expr',1,'p_expr','powrser.py',57),
  ('expr -> if_statement','expr',1,'p_expr','powrser.py',58),
  ('expr -> while_statement','expr',1,'p_expr','powrser.py',59),
  ('expr -> exit_statement','expr',1,'p_expr','powrser.py',60),
  ('expr -> for_statement','expr',1,'p_expr','powrser.py',61),
  ('pow_type -> TYPE_BOOL','pow_type',1,'p_pow_type','powrser.py',68),
  ('pow_type -> TYPE_NUM','pow_type',1,'p_pow_type','powrser.py',69),
  ('pow_type -> TYPE_STR','pow_type',1,'p_pow_type','powrser.py',70),
  ('pow_type -> TYPE_LIST','pow_type',1,'p_pow_type','powrser.py',71),
  ('variable -> ID','variable',1,'p_variable','powrser.py',75),
  ('list_access -> LPAREN expr COLUMN expr RPAREN','list_access',5,'p_list_access','powrser.py',79),
  ('list_expr -> LPAREN RPAREN','list_expr',2,'p_list_expr','powrser.py',83),
  ('list_expr -> LPAREN sequence RPAREN','list_expr',3,'p_list_expr','powrser.py',84),
  ('lambda_expr -> AT variable','lambda_expr',2,'p_lambda_expr','powrser.py',91),
  ('if_statement -> LBRACKET QUESTION expr COLUMN statements RBRACKET','if_statement',6,'p_if_statement','powrser.py',95),
  ('if_statement -> LBRACKET QUESTION expr COLUMN statements SEMI statements RBRACKET','if_statement',8,'p_if_statement','powrser.py',96),
  ('while_statement -> LBRACKET WHILE expr COLUMN statements RBRACKET','while_statement',6,'p_while_statement','powrser.py',103),
  ('exit_statement -> LBRACKET EXIT RBRACKET','exit_statement',3,'p_exit_statement','powrser.py',107),
  ('exit_statement -> LBRACKET EXIT expr RBRACKET','exit_statement',4,'p_exit_statement','powrser.py',108),
  ('command -> SKIP','command',1,'p_command_skip','powrser.py',113),
  ('for_statement -> LBRACKET FOR ID expr expr COLUMN statements RBRACKET','for_statement',8,'p_for_statement','powrser.py',117),
  ('for_statement -> LBRACKET FOR ID expr expr expr COLUMN statements RBRACKET','for_statement',9,'p_for_statement','powrser.py',118),
  ('expr -> MINUS expr','expr',2,'p_expr_uminus','powrser.py',125),
  ('command -> IS expr','command',2,'p_is_command','powrser.py',129),
  ('command -> ECHO','command',1,'p_command_echo','powrser.py',133),
  ('command -> ECHO sequence','command',2,'p_command_echo','powrser.py',134),
  ('command -> READ','command',1,'p_command_read','powrser.py',141),
  ('command -> READ sequence','command',2,'p_command_read','powrser.py',142),
  ('command -> EXPECT pow_type expr','command',3,'p_command_expect','powrser.py',149),
  ('command -> PLUS expr expr','command',3,'p_command_binop','powrser.py',153),
  ('command -> MINUS expr expr','command',3,'p_command_binop','powrser.py',154),
  ('command -> MUL expr expr','command',3,'p_command_binop','powrser.py',155),
  ('command -> DIV expr expr','command',3,'p_command_binop','powrser.py',156),
  ('command -> IDIV expr expr','command',3,'p_command_binop','powrser.py',157),
  ('command -> MOD expr expr','command',3,'p_command_binop','powrser.py',158),
  ('command -> POW expr expr','command',3,'p_command_binop','powrser.py',159),
  ('command -> EQ expr expr','command',3,'p_command_binop','powrser.py',160),
  ('command -> NE expr expr','command',3,'p_command_binop','powrser.py',161),
  ('command -> LT expr expr','command',3,'p_command_binop','powrser.py',162),
  ('command -> LE expr expr','command',3,'p_command_binop','powrser.py',163),
  ('command -> GT expr expr','command',3,'p_command_binop','powrser.py',164),
  ('command -> GE expr expr','command',3,'p_command_binop','powrser.py',165),
  ('command -> PLUSONE expr','command',2,'p_command_plus_one','powrser.py',169),
  ('command -> MINUSONE expr','command',2,'p_command_minus_one','powrser.py',173),
  ('command -> INC ID','command',2,'p_command_incdec','powrser.py',177),
  ('command -> DEC ID','command',2,'p_command_incdec','powrser.py',178),
  ('command -> POW2 expr','command',2,'p_command_pow2','powrser.py',182),
  ('command -> AND expr expr','command',3,'p_command_boolop','powrser.py',186),
  ('command -> OR expr expr','command',3,'p_command_boolop','powrser.py',187),
  ('command -> XOR expr expr','command',3,'p_command_boolop','powrser.py',188),
  ('command -> NOT expr','command',2,'p_command_boolop','powrser.py',189),
  ('command -> HEAD expr','command',2,'p_command_listcmd','powrser.py',198),
  ('command -> TAIL expr','command',2,'p_command_listcmd','powrser.py',199),
  ('command -> LEN expr','command',2,'p_command_listcmd','powrser.py',200),
  ('command -> MAP expr expr','command',3,'p_command_listcmd','powrser.py',201),
  ('command -> FILTER expr expr','command',3,'p_command_listcmd','powrser.py',202),
  ('command -> TYPE expr','command',2,'p_command_type','powrser.py',210),
  ('command -> TOSTR expr','command',2,'p_command_tostr','powrser.py',214),
  ('command -> TONUM expr','command',2,'p_command_tonum','powrser.py',218),
  ('command -> CHAR expr','command',2,'p_command_char','powrser.py',222),
  ('command -> ORD expr','command',2,'p_command_ord','powrser.py',226),
  ('command -> SET ID expr','command',3,'p_command_set','powrser.py',230),
  ('command -> SET LPAREN ID COLUMN expr RPAREN expr','command',7,'p_command_set','powrser.py',231),
  ('command -> SETG ID expr','command',3,'p_command_setg','powrser.py',238),
  ('command -> SETG LPAREN ID COLUMN expr RPAREN expr','command',7,'p_command_setg','powrser.py',239),
  ('command -> PUSH ID sequence','command',3,'p_command_push','powrser.py',246),
  ('command -> POP ID','command',2,'p_command_pop','powrser.py',250),
  ('command -> POP ID expr','command',3,'p_command_pop','powrser.py',251),
  ('command -> DEF ID LBRACKET RBRACKET COLUMN statements','command',6,'p_command_def','powrser.py',258),
  ('command -> DEF ID LBRACKET id_sequence RBRACKET COLUMN statements','command',7,'p_command_def','powrser.py',259),
  ('command -> ID','command',1,'p_command_call','powrser.py',266),
  ('command -> ID sequence','command',2,'p_command_call','powrser.py',267),
  ('command -> LAMBDA LBRACKET RBRACKET COLUMN expr','command',5,'p_command_lambda','powrser.py',274),
  ('command -> LAMBDA LBRACKET id_sequence RBRACKET COLUMN expr','command',6,'p_command_lambda','powrser.py',275),
  ('command -> AT ID','command',2,'p_command_lambdacall','powrser.py',282),
  ('command -> AT ID sequence','command',3,'p_command_lambdacall','powrser.py',283),
  ('command -> DEL ID','command',2,'p_command_del','powrser.py',290),
  ('command -> RND','command',1,'p_command_rnd','powrser.py',294),
  ('command -> TIME','command',1,'p_command_time','powrser.py',298),
  ('command -> PAUSE expr','command',2,'p_command_pause','powrser.py',302),
  ('command -> GETCUR','command',1,'p_command_getcur','powrser.py',306),
  ('command -> SCRSIZE','command',1,'p_command_scrsize','powrser.py',310),
  ('command -> USES ID','command',2,'p_command_uses','powrser.py',314),
]
