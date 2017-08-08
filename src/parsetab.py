
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightUMINUSNULL NUMBER BOOL STRING EQ NE GT GE LT LE PLUS MINUS MUL DIV IDIV MOD POW POW2 INC DEC PLUSONE MINUSONE LPAREN RPAREN LBRACKET RBRACKET AT QUESTION COLUMN SEMI IS ID TYPE_BOOL TYPE_NUM TYPE_STR TYPE_LIST ECHO READ EXPECT SET DEL FOR WHILE EXIT DEF LAMBDA LEN NOT AND OR XOR RND HEAD TAIL PUSH POP MAP FILTER TYPE TOSTR TONUM USES GETCUR SCRSIZE TIME PAUSEstatements : statement\n                  | statements statementstatement : exprsequence : element\n                | sequence elementelement : expr id_sequence : id_element\n                    | id_sequence id_elementid_element : IDexpr : LBRACKET command RBRACKET\n            | STRING\n            | NUMBER\n            | BOOL\n            | NULL\n            | pow_type\n            | variable\n            | list_expr\n            | list_access\n            | lambda_expr\n            | if_statement\n            | while_statement\n            | exit_statement\n            | for_statementpow_type : TYPE_BOOL\n                | TYPE_NUM\n                | TYPE_STR\n                | TYPE_LISTvariable : IDlist_access : LPAREN expr COLUMN expr RPARENlist_expr : LPAREN RPAREN\n                 | LPAREN sequence RPARENlambda_expr : AT variableif_statement : LBRACKET QUESTION expr COLUMN statements RBRACKET\n                    | LBRACKET QUESTION expr COLUMN statements SEMI statements RBRACKETwhile_statement : LBRACKET WHILE expr COLUMN statements RBRACKETexit_statement : LBRACKET EXIT RBRACKET\n                      | LBRACKET EXIT expr RBRACKETfor_statement : LBRACKET FOR ID expr expr COLUMN statements RBRACKET\n                     | LBRACKET FOR ID expr expr expr COLUMN statements RBRACKETexpr : MINUS expr %prec UMINUScommand : IS exprcommand : ECHO\n               | ECHO sequencecommand : READ\n               | READ sequencecommand : EXPECT pow_type exprcommand : PLUS  expr expr\n               | MINUS expr expr\n               | MUL   expr expr\n               | DIV   expr expr\n               | IDIV  expr expr\n               | MOD   expr expr\n               | POW   expr expr\n               | EQ    expr expr\n               | NE    expr expr\n               | LT    expr expr\n               | LE    expr expr\n               | GT    expr expr\n               | GE    expr exprcommand : PLUSONE exprcommand : MINUSONE exprcommand : INC ID\n               | DEC IDcommand : POW2 exprcommand : AND expr expr\n               | OR  expr expr\n               | XOR expr expr\n               | NOT exprcommand : HEAD expr\n               | TAIL expr\n               | LEN  expr\n               | MAP expr expr\n               | FILTER expr exprcommand : TYPE exprcommand : TOSTR exprcommand : TONUM exprcommand : SET ID expr\n               | SET LPAREN ID COLUMN expr RPAREN exprcommand : PUSH ID sequencecommand : POP ID\n               | POP ID exprcommand : DEF ID LBRACKET RBRACKET COLUMN statements\n               | DEF ID LBRACKET id_sequence RBRACKET COLUMN statementscommand : ID\n               | ID sequencecommand : LAMBDA LBRACKET RBRACKET COLUMN expr\n               | LAMBDA LBRACKET id_sequence RBRACKET COLUMN exprcommand : AT ID\n               | AT ID sequencecommand : DEL IDcommand : RNDcommand : TIMEcommand : PAUSE exprcommand : GETCURcommand : SCRSIZEcommand : USES ID'
    
_lr_action_items = {'LBRACKET':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,71,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,132,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[4,4,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,4,-24,-25,-26,-27,-28,4,-2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,133,4,-40,-30,4,-6,-4,-32,-10,-36,4,4,-6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,168,4,-31,-5,4,4,4,-37,4,4,4,4,4,4,4,4,-29,-33,4,-35,4,4,4,4,4,4,4,4,4,-34,4,-38,4,-39,]),'STRING':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[5,5,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,5,-24,-25,-26,-27,-28,5,-2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-40,-30,5,-6,-4,-32,-10,-36,5,5,-6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-31,-5,5,5,5,-37,5,5,5,5,5,5,5,5,-29,-33,5,-35,5,5,5,5,5,5,5,5,5,-34,5,-38,5,-39,]),'NUMBER':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[6,6,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,6,-24,-25,-26,-27,-28,6,-2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-40,-30,6,-6,-4,-32,-10,-36,6,6,-6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-31,-5,6,6,6,-37,6,6,6,6,6,6,6,6,-29,-33,6,-35,6,6,6,6,6,6,6,6,6,-34,6,-38,6,-39,]),'BOOL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[7,7,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,7,-24,-25,-26,-27,-28,7,-2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-40,-30,7,-6,-4,-32,-10,-36,7,7,-6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-31,-5,7,7,7,-37,7,7,7,7,7,7,7,7,-29,-33,7,-35,7,7,7,7,7,7,7,7,7,-34,7,-38,7,-39,]),'NULL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[8,8,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,8,-24,-25,-26,-27,-28,8,-2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-40,-30,8,-6,-4,-32,-10,-36,8,8,-6,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-31,-5,8,8,8,-37,8,8,8,8,8,8,8,8,-29,-33,8,-35,8,8,8,8,8,8,8,8,8,-34,8,-38,8,-39,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[18,18,-1,-3,38,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,18,-24,-25,-26,-27,-28,18,-2,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-40,-30,18,-6,-4,-32,-10,-36,18,18,-6,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-31,-5,18,18,18,-37,18,18,18,18,18,18,18,18,-29,-33,18,-35,18,18,18,18,18,18,18,18,18,-34,18,-38,18,-39,]),'TYPE_BOOL':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[19,19,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,19,-24,-25,-26,-27,-28,19,-2,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-40,-30,19,-6,-4,-32,-10,-36,19,19,-6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-31,-5,19,19,19,-37,19,19,19,19,19,19,19,19,-29,-33,19,-35,19,19,19,19,19,19,19,19,19,-34,19,-38,19,-39,]),'TYPE_NUM':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[20,20,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,20,-24,-25,-26,-27,-28,20,-2,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-40,-30,20,-6,-4,-32,-10,-36,20,20,-6,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-31,-5,20,20,20,-37,20,20,20,20,20,20,20,20,-29,-33,20,-35,20,20,20,20,20,20,20,20,20,-34,20,-38,20,-39,]),'TYPE_STR':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[21,21,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,21,-24,-25,-26,-27,-28,21,-2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-40,-30,21,-6,-4,-32,-10,-36,21,21,-6,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-31,-5,21,21,21,-37,21,21,21,21,21,21,21,21,-29,-33,21,-35,21,21,21,21,21,21,21,21,21,-34,21,-38,21,-39,]),'TYPE_LIST':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[22,22,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,22,-24,-25,-26,-27,-28,22,-2,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-40,-30,22,-6,-4,-32,-10,-36,22,22,-6,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-31,-5,22,22,22,-37,22,22,22,22,22,22,22,22,-29,-33,22,-35,22,22,22,22,22,22,22,22,22,-34,22,-38,22,-39,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,76,79,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,129,130,131,133,134,138,139,140,141,142,143,144,166,168,170,171,172,173,175,176,177,178,180,181,183,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[23,23,-1,-3,32,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,23,-24,-25,-26,-27,-28,23,23,-2,23,23,23,91,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,113,114,23,23,23,23,23,23,23,23,23,23,23,23,23,128,130,131,132,134,135,23,137,-40,-30,23,-6,-4,-32,-10,-36,23,23,-6,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,165,23,23,172,23,-31,-5,23,23,23,-37,23,23,172,172,-7,-9,23,23,23,23,23,172,23,-8,-29,-33,23,-35,23,23,23,23,23,23,23,23,23,-34,23,-38,23,-39,]),'LPAREN':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[24,24,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,24,-24,-25,-26,-27,-28,24,-2,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,129,24,-40,-30,24,-6,-4,-32,-10,-36,24,24,-6,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-31,-5,24,24,24,-37,24,24,24,24,24,24,24,24,-29,-33,24,-35,24,24,24,24,24,24,24,24,24,-34,24,-38,24,-39,]),'AT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,80,81,82,83,84,85,86,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,138,139,140,141,142,143,144,166,173,175,176,177,178,181,184,185,186,187,189,191,194,195,196,197,198,199,200,202,203,204,206,207,],[25,25,-1,-3,72,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,25,-24,-25,-26,-27,-28,25,-2,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-40,-30,25,-6,-4,-32,-10,-36,25,25,-6,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-31,-5,25,25,25,-37,25,25,25,25,25,25,25,25,-29,-33,25,-35,25,25,25,25,25,25,25,25,25,-34,25,-38,25,-39,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,80,81,85,86,89,138,143,184,185,187,202,204,207,],[0,-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,-40,-30,-32,-10,-36,-31,-37,-29,-33,-35,-34,-38,-39,]),'RBRACKET':([2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,27,30,32,34,35,74,75,77,78,80,81,84,85,86,89,90,92,93,94,95,96,111,112,113,114,115,119,120,121,122,125,126,127,131,133,134,135,136,137,138,139,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,166,167,168,170,171,172,173,175,176,180,183,184,185,187,193,195,197,199,201,202,203,204,205,206,207,],[-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,86,89,-84,-42,-44,-91,-92,-94,-95,-40,-30,-4,-32,-10,-36,143,-85,-6,-41,-43,-45,-60,-61,-62,-63,-64,-68,-69,-70,-71,-74,-75,-76,-80,169,-88,-90,-93,-96,-31,-5,-37,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-65,-66,-67,-72,-73,-77,-79,-81,179,182,-7,-9,-89,185,187,192,-8,-29,-33,-35,-86,202,204,-82,-87,-34,207,-38,-78,-83,-39,]),'SEMI':([2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,26,80,81,85,86,89,138,143,175,184,185,187,202,204,207,],[-1,-3,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-2,-40,-30,-32,-10,-36,-31,-37,186,-29,-33,-35,-34,-38,-39,]),'QUESTION':([4,],[28,]),'WHILE':([4,],[29,]),'EXIT':([4,],[30,]),'FOR':([4,],[31,]),'IS':([4,],[33,]),'ECHO':([4,],[34,]),'READ':([4,],[35,]),'EXPECT':([4,],[36,]),'PLUS':([4,],[37,]),'MUL':([4,],[39,]),'DIV':([4,],[40,]),'IDIV':([4,],[41,]),'MOD':([4,],[42,]),'POW':([4,],[43,]),'EQ':([4,],[44,]),'NE':([4,],[45,]),'LT':([4,],[46,]),'LE':([4,],[47,]),'GT':([4,],[48,]),'GE':([4,],[49,]),'PLUSONE':([4,],[50,]),'MINUSONE':([4,],[51,]),'INC':([4,],[52,]),'DEC':([4,],[53,]),'POW2':([4,],[54,]),'AND':([4,],[55,]),'OR':([4,],[56,]),'XOR':([4,],[57,]),'NOT':([4,],[58,]),'HEAD':([4,],[59,]),'TAIL':([4,],[60,]),'LEN':([4,],[61,]),'MAP':([4,],[62,]),'FILTER':([4,],[63,]),'TYPE':([4,],[64,]),'TOSTR':([4,],[65,]),'TONUM':([4,],[66,]),'SET':([4,],[67,]),'PUSH':([4,],[68,]),'POP':([4,],[69,]),'DEF':([4,],[70,]),'LAMBDA':([4,],[71,]),'DEL':([4,],[73,]),'RND':([4,],[74,]),'TIME':([4,],[75,]),'PAUSE':([4,],[76,]),'GETCUR':([4,],[77,]),'SCRSIZE':([4,],[78,]),'USES':([4,],[79,]),'COLUMN':([5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,80,81,83,85,86,87,88,89,138,143,165,169,177,179,182,184,185,187,188,192,202,204,207,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-40,-30,140,-32,-10,141,142,-36,-31,-37,178,181,189,191,194,-29,-33,-35,196,200,-34,-38,-39,]),'RPAREN':([5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,80,81,82,83,84,85,86,89,93,138,139,143,174,184,185,187,190,202,204,207,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,81,-40,-30,138,-6,-4,-32,-10,-36,-6,-31,-5,-37,184,-29,-33,-35,198,-34,-38,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,141,142,186,189,191,196,200,],[1,175,176,195,197,199,203,206,]),'statement':([0,1,141,142,175,176,186,189,191,195,196,197,199,200,203,206,],[2,26,2,2,26,26,2,2,2,26,2,26,26,2,26,26,]),'expr':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[3,3,80,83,87,88,90,93,94,93,93,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,122,123,124,125,126,127,136,93,144,93,93,93,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,93,167,93,174,3,3,177,93,93,3,3,188,190,193,3,3,3,201,3,3,3,205,3,3,3,3,]),'pow_type':([0,1,18,24,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[9,9,9,9,9,9,9,9,9,9,9,97,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'variable':([0,1,18,24,25,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[10,10,10,10,85,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'list_expr':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'list_access':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'lambda_expr':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'if_statement':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'while_statement':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'exit_statement':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'for_statement':([0,1,18,24,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,76,82,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,117,118,123,124,128,130,131,134,140,141,142,144,166,173,175,176,177,178,181,186,189,191,194,195,196,197,198,199,200,203,206,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'command':([4,],[27,]),'sequence':([24,32,34,35,130,134,],[82,92,95,96,166,173,]),'element':([24,32,34,35,82,92,95,96,130,134,166,173,],[84,84,84,84,139,139,139,139,84,84,139,139,]),'id_sequence':([133,168,],[170,180,]),'id_element':([133,168,170,180,],[171,171,183,183,]),}

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
  ('for_statement -> LBRACKET FOR ID expr expr COLUMN statements RBRACKET','for_statement',8,'p_for_statement','powrser.py',113),
  ('for_statement -> LBRACKET FOR ID expr expr expr COLUMN statements RBRACKET','for_statement',9,'p_for_statement','powrser.py',114),
  ('expr -> MINUS expr','expr',2,'p_expr_uminus','powrser.py',121),
  ('command -> IS expr','command',2,'p_is_command','powrser.py',125),
  ('command -> ECHO','command',1,'p_command_echo','powrser.py',129),
  ('command -> ECHO sequence','command',2,'p_command_echo','powrser.py',130),
  ('command -> READ','command',1,'p_command_read','powrser.py',137),
  ('command -> READ sequence','command',2,'p_command_read','powrser.py',138),
  ('command -> EXPECT pow_type expr','command',3,'p_command_expect','powrser.py',145),
  ('command -> PLUS expr expr','command',3,'p_command_binop','powrser.py',149),
  ('command -> MINUS expr expr','command',3,'p_command_binop','powrser.py',150),
  ('command -> MUL expr expr','command',3,'p_command_binop','powrser.py',151),
  ('command -> DIV expr expr','command',3,'p_command_binop','powrser.py',152),
  ('command -> IDIV expr expr','command',3,'p_command_binop','powrser.py',153),
  ('command -> MOD expr expr','command',3,'p_command_binop','powrser.py',154),
  ('command -> POW expr expr','command',3,'p_command_binop','powrser.py',155),
  ('command -> EQ expr expr','command',3,'p_command_binop','powrser.py',156),
  ('command -> NE expr expr','command',3,'p_command_binop','powrser.py',157),
  ('command -> LT expr expr','command',3,'p_command_binop','powrser.py',158),
  ('command -> LE expr expr','command',3,'p_command_binop','powrser.py',159),
  ('command -> GT expr expr','command',3,'p_command_binop','powrser.py',160),
  ('command -> GE expr expr','command',3,'p_command_binop','powrser.py',161),
  ('command -> PLUSONE expr','command',2,'p_command_plus_one','powrser.py',165),
  ('command -> MINUSONE expr','command',2,'p_command_minus_one','powrser.py',169),
  ('command -> INC ID','command',2,'p_command_incdec','powrser.py',173),
  ('command -> DEC ID','command',2,'p_command_incdec','powrser.py',174),
  ('command -> POW2 expr','command',2,'p_command_pow2','powrser.py',178),
  ('command -> AND expr expr','command',3,'p_command_boolop','powrser.py',182),
  ('command -> OR expr expr','command',3,'p_command_boolop','powrser.py',183),
  ('command -> XOR expr expr','command',3,'p_command_boolop','powrser.py',184),
  ('command -> NOT expr','command',2,'p_command_boolop','powrser.py',185),
  ('command -> HEAD expr','command',2,'p_command_listcmd','powrser.py',194),
  ('command -> TAIL expr','command',2,'p_command_listcmd','powrser.py',195),
  ('command -> LEN expr','command',2,'p_command_listcmd','powrser.py',196),
  ('command -> MAP expr expr','command',3,'p_command_listcmd','powrser.py',197),
  ('command -> FILTER expr expr','command',3,'p_command_listcmd','powrser.py',198),
  ('command -> TYPE expr','command',2,'p_command_type','powrser.py',206),
  ('command -> TOSTR expr','command',2,'p_command_tostr','powrser.py',210),
  ('command -> TONUM expr','command',2,'p_command_tonum','powrser.py',214),
  ('command -> SET ID expr','command',3,'p_command_set','powrser.py',218),
  ('command -> SET LPAREN ID COLUMN expr RPAREN expr','command',7,'p_command_set','powrser.py',219),
  ('command -> PUSH ID sequence','command',3,'p_command_push','powrser.py',226),
  ('command -> POP ID','command',2,'p_command_pop','powrser.py',230),
  ('command -> POP ID expr','command',3,'p_command_pop','powrser.py',231),
  ('command -> DEF ID LBRACKET RBRACKET COLUMN statements','command',6,'p_command_def','powrser.py',238),
  ('command -> DEF ID LBRACKET id_sequence RBRACKET COLUMN statements','command',7,'p_command_def','powrser.py',239),
  ('command -> ID','command',1,'p_command_call','powrser.py',246),
  ('command -> ID sequence','command',2,'p_command_call','powrser.py',247),
  ('command -> LAMBDA LBRACKET RBRACKET COLUMN expr','command',5,'p_command_lambda','powrser.py',254),
  ('command -> LAMBDA LBRACKET id_sequence RBRACKET COLUMN expr','command',6,'p_command_lambda','powrser.py',255),
  ('command -> AT ID','command',2,'p_command_lambdacall','powrser.py',262),
  ('command -> AT ID sequence','command',3,'p_command_lambdacall','powrser.py',263),
  ('command -> DEL ID','command',2,'p_command_del','powrser.py',270),
  ('command -> RND','command',1,'p_command_rnd','powrser.py',274),
  ('command -> TIME','command',1,'p_command_time','powrser.py',278),
  ('command -> PAUSE expr','command',2,'p_command_pause','powrser.py',282),
  ('command -> GETCUR','command',1,'p_command_getcur','powrser.py',286),
  ('command -> SCRSIZE','command',1,'p_command_scrsize','powrser.py',290),
  ('command -> USES ID','command',2,'p_command_uses','powrser.py',294),
]
