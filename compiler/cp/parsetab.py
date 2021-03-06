
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'SINO SI E S F AND OR MQ for H PLUS MINUS TIMES DIVIDE POW MODULO LESS LESSEQUAL GREATER GREATEREQUAL EQUAL DEQUAL DISTINT SEMICOLON COMMA LPAREN RPAREN LBRACKET RBRACKET LBLOCK RBLOCK ID NUMBERprogram : declaration_listdeclaration_list : declaration_list declarationdeclaration_list : declarationdeclaration : var_declaration\n\t\t\t\t  | fun_declarationvar_declaration : type_specifier ID SEMICOLONvar_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLONvar_declaration : type_specifier ID COMMA ID SEMICOLONtype_specifier : Etype_specifier : Stype_specifier : Ffun_declaration : type_specifier ID LPAREN params RPAREN compount_stmtparams : param_listparam_list : param_list COMMA paramparam_list : paramparam_list : emptyparam : type_specifier IDparam : type_specifier ID LBRACKET RBRACKETcompount_stmt : LBLOCK local_declarations statement_list RBLOCKlocal_declarations : local_declarations var_declarationlocal_declarations : emptystatement_list : statement_list statementstatement_list : emptyselection_stmt : SI LPAREN expression RPAREN statementselection_stmt : SI LPAREN expression RPAREN statement SINO statementiteration_stmt : MQ LPAREN expression RPAREN statementiteration_stmt : H  statement  MQ LPAREN expression RPARENiteration_stmt : for LPAREN ID EQUAL NUMBER SEMICOLON ID relop NUMBER SEMICOLON ID addop addop RPAREN statementstatement : expression_stmt\n\t\t\t\t| compount_stmt\n\t\t\t\t| selection_stmt\n\t\t\t\t| iteration_stmt\n\t\t\t\t\n\texpression_stmt : expression SEMICOLONexpression_stmt : SEMICOLONexpression : var EQUAL expressionexpression : simple_expressionvar : IDvar : ID LBRACKET expression RBRACKETsimple_expression : additive_expression relop additive_expressionsimple_expression : additive_expressionrelop : LESS \n\t\t\t| LESSEQUAL\n\t\t\t| GREATER\n\t\t\t| GREATEREQUAL\n\t\t\t| DEQUAL\n\t\t\t| DISTINT\n\t\t\t| AND\n\t\t\t| OR\n\tadditive_expression : additive_expression addop termadditive_expression : termaddop : PLUS \n\t\t\t| MINUS\n\tterm : term mulop factorterm : factormulop : \tTIMES\n\t\t\t\t| DIVIDE\n\t            | POW\n   \t            | MODULO\n\n\tfactor : LPAREN expression RPARENfactor : varfactor : callfactor : NUMBERcall : ID LPAREN args RPARENargs : args_list\n\t\t\t| empty\n\targs_list : args_list COMMA expressionargs_list : expressionempty :'
    
_lr_action_items = {'E':([0,2,3,4,5,10,12,15,24,27,28,30,31,34,35,37,40,],[7,7,-3,-4,-5,-2,-6,7,-8,7,-7,-12,-68,7,-21,-20,-19,]),'S':([0,2,3,4,5,10,12,15,24,27,28,30,31,34,35,37,40,],[8,8,-3,-4,-5,-2,-6,8,-8,8,-7,-12,-68,8,-21,-20,-19,]),'F':([0,2,3,4,5,10,12,15,24,27,28,30,31,34,35,37,40,],[9,9,-3,-4,-5,-2,-6,9,-8,9,-7,-12,-68,9,-21,-20,-19,]),'$end':([1,2,3,4,5,10,12,24,28,30,40,],[0,-1,-3,-4,-5,-2,-6,-8,-7,-12,-19,]),'ID':([6,7,8,9,12,14,18,24,28,31,34,35,36,37,38,39,40,41,42,43,44,45,47,49,51,62,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,103,104,105,109,110,111,115,116,117,118,122,126,127,],[11,-9,-10,-11,-6,17,25,-8,-7,-68,-68,-21,53,-20,-23,61,-19,-22,-29,-30,-31,-32,-34,53,53,-33,53,53,92,53,53,53,53,53,-41,-42,-43,-44,-45,-46,-47,-48,-51,-52,53,-55,-56,-57,-58,53,53,53,53,-24,-26,53,-27,119,-25,123,53,-28,]),'SEMICOLON':([11,12,17,23,24,28,31,34,35,36,37,38,40,41,42,43,44,45,46,47,51,53,54,55,56,57,58,59,60,61,62,89,98,99,100,101,102,103,104,107,108,110,111,113,115,116,118,121,126,127,],[12,-6,24,28,-8,-7,-68,-68,-21,47,-20,-23,-19,-22,-29,-30,-31,-32,62,-34,47,-37,-62,-60,-36,-40,-50,-54,-61,12,-33,-59,-35,-39,-60,-49,-53,47,47,-38,-63,-24,-26,117,47,-27,-25,122,47,-28,]),'LBRACKET':([11,25,53,61,],[13,29,68,13,]),'COMMA':([11,15,20,21,22,25,32,33,53,54,55,56,57,58,59,60,61,89,95,97,98,99,100,101,102,107,108,114,],[14,-68,27,-15,-16,-17,-14,-18,-37,-62,-60,-36,-40,-50,-54,-61,14,-59,109,-67,-35,-39,-60,-49,-53,-38,-63,-66,]),'LPAREN':([11,12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,48,49,50,51,52,53,62,63,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,103,104,105,109,110,111,115,116,118,126,127,],[15,-6,-8,-7,-68,-68,-21,49,-20,-23,-19,-22,-29,-30,-31,-32,-34,63,49,65,49,67,69,-33,49,49,49,49,49,49,49,-41,-42,-43,-44,-45,-46,-47,-48,-51,-52,49,-55,-56,-57,-58,105,49,49,49,49,-24,-26,49,-27,-25,49,-28,]),'RBLOCK':([12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,62,110,111,116,118,127,],[-6,-8,-7,-68,-68,-21,40,-20,-23,-19,-22,-29,-30,-31,-32,-34,-33,-24,-26,-27,-25,-28,]),'LBLOCK':([12,24,26,28,31,34,35,36,37,38,40,41,42,43,44,45,47,51,62,103,104,110,111,115,116,118,126,127,],[-6,-8,31,-7,-68,-68,-21,31,-20,-23,-19,-22,-29,-30,-31,-32,-34,31,-33,31,31,-24,-26,31,-27,-25,31,-28,]),'SI':([12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,51,62,103,104,110,111,115,116,118,126,127,],[-6,-8,-7,-68,-68,-21,48,-20,-23,-19,-22,-29,-30,-31,-32,-34,48,-33,48,48,-24,-26,48,-27,-25,48,-28,]),'MQ':([12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,51,62,66,103,104,110,111,115,116,118,126,127,],[-6,-8,-7,-68,-68,-21,50,-20,-23,-19,-22,-29,-30,-31,-32,-34,50,-33,91,50,50,-24,-26,50,-27,-25,50,-28,]),'H':([12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,51,62,103,104,110,111,115,116,118,126,127,],[-6,-8,-7,-68,-68,-21,51,-20,-23,-19,-22,-29,-30,-31,-32,-34,51,-33,51,51,-24,-26,51,-27,-25,51,-28,]),'for':([12,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,51,62,103,104,110,111,115,116,118,126,127,],[-6,-8,-7,-68,-68,-21,52,-20,-23,-19,-22,-29,-30,-31,-32,-34,52,-33,52,52,-24,-26,52,-27,-25,52,-28,]),'NUMBER':([12,13,24,28,31,34,35,36,37,38,40,41,42,43,44,45,47,49,51,62,63,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,103,104,105,106,109,110,111,115,116,118,120,126,127,],[-6,16,-8,-7,-68,-68,-21,54,-20,-23,-19,-22,-29,-30,-31,-32,-34,54,54,-33,54,54,54,54,54,54,54,-41,-42,-43,-44,-45,-46,-47,-48,-51,-52,54,-55,-56,-57,-58,54,54,54,113,54,-24,-26,54,-27,-25,121,54,-28,]),'RPAREN':([15,19,20,21,22,25,32,33,53,54,55,56,57,58,59,60,64,69,81,82,88,89,90,94,95,96,97,98,99,100,101,102,107,108,112,114,125,],[-68,26,-13,-15,-16,-17,-14,-18,-37,-62,-60,-36,-40,-50,-54,-61,89,-68,-51,-52,103,-59,104,108,-64,-65,-67,-35,-39,-60,-49,-53,-38,-63,116,-66,126,]),'RBRACKET':([16,29,53,54,55,56,57,58,59,60,89,93,98,99,100,101,102,107,108,],[23,33,-37,-62,-60,-36,-40,-50,-54,-61,-59,107,-35,-39,-60,-49,-53,-38,-63,]),'SINO':([40,42,43,44,45,47,62,110,111,116,118,127,],[-19,-29,-30,-31,-32,-34,-33,115,-26,-27,-25,-28,]),'EQUAL':([53,55,92,107,],[-37,70,106,-38,]),'TIMES':([53,54,55,58,59,60,89,100,101,102,107,108,],[-37,-62,-60,84,-54,-61,-59,-60,84,-53,-38,-63,]),'DIVIDE':([53,54,55,58,59,60,89,100,101,102,107,108,],[-37,-62,-60,85,-54,-61,-59,-60,85,-53,-38,-63,]),'POW':([53,54,55,58,59,60,89,100,101,102,107,108,],[-37,-62,-60,86,-54,-61,-59,-60,86,-53,-38,-63,]),'MODULO':([53,54,55,58,59,60,89,100,101,102,107,108,],[-37,-62,-60,87,-54,-61,-59,-60,87,-53,-38,-63,]),'LESS':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,73,-50,-54,-61,-59,-60,-49,-53,-38,-63,73,]),'LESSEQUAL':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,74,-50,-54,-61,-59,-60,-49,-53,-38,-63,74,]),'GREATER':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,75,-50,-54,-61,-59,-60,-49,-53,-38,-63,75,]),'GREATEREQUAL':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,76,-50,-54,-61,-59,-60,-49,-53,-38,-63,76,]),'DEQUAL':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,77,-50,-54,-61,-59,-60,-49,-53,-38,-63,77,]),'DISTINT':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,78,-50,-54,-61,-59,-60,-49,-53,-38,-63,78,]),'AND':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,79,-50,-54,-61,-59,-60,-49,-53,-38,-63,79,]),'OR':([53,54,55,57,58,59,60,89,100,101,102,107,108,119,],[-37,-62,-60,80,-50,-54,-61,-59,-60,-49,-53,-38,-63,80,]),'PLUS':([53,54,55,57,58,59,60,81,82,89,99,100,101,102,107,108,123,124,],[-37,-62,-60,81,-50,-54,-61,-51,-52,-59,81,-60,-49,-53,-38,-63,81,81,]),'MINUS':([53,54,55,57,58,59,60,81,82,89,99,100,101,102,107,108,123,124,],[-37,-62,-60,82,-50,-54,-61,-51,-52,-59,82,-60,-49,-53,-38,-63,82,82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,10,]),'var_declaration':([0,2,34,],[4,4,37,]),'fun_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,15,27,34,],[6,6,18,18,39,]),'params':([15,],[19,]),'param_list':([15,],[20,]),'param':([15,27,],[21,32,]),'empty':([15,31,34,69,],[22,35,38,96,]),'compount_stmt':([26,36,51,103,104,115,126,],[30,43,43,43,43,43,43,]),'local_declarations':([31,],[34,]),'statement_list':([34,],[36,]),'statement':([36,51,103,104,115,126,],[41,66,110,111,118,127,]),'expression_stmt':([36,51,103,104,115,126,],[42,42,42,42,42,42,]),'selection_stmt':([36,51,103,104,115,126,],[44,44,44,44,44,44,]),'iteration_stmt':([36,51,103,104,115,126,],[45,45,45,45,45,45,]),'expression':([36,49,51,63,65,68,69,70,103,104,105,109,115,126,],[46,64,46,88,90,93,97,98,46,46,112,114,46,46,]),'var':([36,49,51,63,65,68,69,70,71,72,83,103,104,105,109,115,126,],[55,55,55,55,55,55,55,55,100,100,100,55,55,55,55,55,55,]),'simple_expression':([36,49,51,63,65,68,69,70,103,104,105,109,115,126,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'additive_expression':([36,49,51,63,65,68,69,70,71,103,104,105,109,115,126,],[57,57,57,57,57,57,57,57,99,57,57,57,57,57,57,]),'term':([36,49,51,63,65,68,69,70,71,72,103,104,105,109,115,126,],[58,58,58,58,58,58,58,58,58,101,58,58,58,58,58,58,]),'factor':([36,49,51,63,65,68,69,70,71,72,83,103,104,105,109,115,126,],[59,59,59,59,59,59,59,59,59,59,102,59,59,59,59,59,59,]),'call':([36,49,51,63,65,68,69,70,71,72,83,103,104,105,109,115,126,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'relop':([57,119,],[71,120,]),'addop':([57,99,123,124,],[72,72,124,125,]),'mulop':([58,101,],[83,83,]),'args':([69,],[94,]),'args_list':([69,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','_parser.py',10),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_1','_parser.py',14),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list_2','_parser.py',19),
  ('declaration -> var_declaration','declaration',1,'p_declaration','_parser.py',23),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','_parser.py',24),
  ('var_declaration -> type_specifier ID SEMICOLON','var_declaration',3,'p_var_declaration_1','_parser.py',28),
  ('var_declaration -> type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON','var_declaration',6,'p_var_declaration_2','_parser.py',32),
  ('var_declaration -> type_specifier ID COMMA ID SEMICOLON','var_declaration',5,'p_var_declaration_3','_parser.py',37),
  ('type_specifier -> E','type_specifier',1,'p_type_specifier_1','_parser.py',47),
  ('type_specifier -> S','type_specifier',1,'p_type_specifier_2','_parser.py',51),
  ('type_specifier -> F','type_specifier',1,'p_type_specifier_3','_parser.py',55),
  ('fun_declaration -> type_specifier ID LPAREN params RPAREN compount_stmt','fun_declaration',6,'p_fun_declaration','_parser.py',65),
  ('params -> param_list','params',1,'p_params_1','_parser.py',70),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_1','_parser.py',74),
  ('param_list -> param','param_list',1,'p_param_list_2','_parser.py',78),
  ('param_list -> empty','param_list',1,'p_param_list_3','_parser.py',82),
  ('param -> type_specifier ID','param',2,'p_param_1','_parser.py',86),
  ('param -> type_specifier ID LBRACKET RBRACKET','param',4,'p_param_2','_parser.py',90),
  ('compount_stmt -> LBLOCK local_declarations statement_list RBLOCK','compount_stmt',4,'p_compount_stmt','_parser.py',94),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations_1','_parser.py',98),
  ('local_declarations -> empty','local_declarations',1,'p_local_declarations_2','_parser.py',102),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_1','_parser.py',106),
  ('statement_list -> empty','statement_list',1,'p_statement_list_2','_parser.py',110),
  ('selection_stmt -> SI LPAREN expression RPAREN statement','selection_stmt',5,'p_selection_stmt_1','_parser.py',117),
  ('selection_stmt -> SI LPAREN expression RPAREN statement SINO statement','selection_stmt',7,'p_selection_stmt_2','_parser.py',121),
  ('iteration_stmt -> MQ LPAREN expression RPAREN statement','iteration_stmt',5,'p_iteration_stmt_1','_parser.py',129),
  ('iteration_stmt -> H statement MQ LPAREN expression RPAREN','iteration_stmt',6,'p_iteration_stmt_2','_parser.py',133),
  ('iteration_stmt -> for LPAREN ID EQUAL NUMBER SEMICOLON ID relop NUMBER SEMICOLON ID addop addop RPAREN statement','iteration_stmt',15,'p_iteration_stmt_3','_parser.py',138),
  ('statement -> expression_stmt','statement',1,'p_statement','_parser.py',144),
  ('statement -> compount_stmt','statement',1,'p_statement','_parser.py',145),
  ('statement -> selection_stmt','statement',1,'p_statement','_parser.py',146),
  ('statement -> iteration_stmt','statement',1,'p_statement','_parser.py',147),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt_1','_parser.py',153),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt_2','_parser.py',157),
  ('expression -> var EQUAL expression','expression',3,'p_expression_1','_parser.py',161),
  ('expression -> simple_expression','expression',1,'p_expression_2','_parser.py',165),
  ('var -> ID','var',1,'p_var_1','_parser.py',169),
  ('var -> ID LBRACKET expression RBRACKET','var',4,'p_var_2','_parser.py',173),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression_1','_parser.py',177),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression_2','_parser.py',181),
  ('relop -> LESS','relop',1,'p_relop','_parser.py',185),
  ('relop -> LESSEQUAL','relop',1,'p_relop','_parser.py',186),
  ('relop -> GREATER','relop',1,'p_relop','_parser.py',187),
  ('relop -> GREATEREQUAL','relop',1,'p_relop','_parser.py',188),
  ('relop -> DEQUAL','relop',1,'p_relop','_parser.py',189),
  ('relop -> DISTINT','relop',1,'p_relop','_parser.py',190),
  ('relop -> AND','relop',1,'p_relop','_parser.py',191),
  ('relop -> OR','relop',1,'p_relop','_parser.py',192),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression_1','_parser.py',197),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression_2','_parser.py',201),
  ('addop -> PLUS','addop',1,'p_addop','_parser.py',205),
  ('addop -> MINUS','addop',1,'p_addop','_parser.py',206),
  ('term -> term mulop factor','term',3,'p_term_1','_parser.py',211),
  ('term -> factor','term',1,'p_term_2','_parser.py',215),
  ('mulop -> TIMES','mulop',1,'p_mulop','_parser.py',219),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','_parser.py',220),
  ('mulop -> POW','mulop',1,'p_mulop','_parser.py',221),
  ('mulop -> MODULO','mulop',1,'p_mulop','_parser.py',222),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_1','_parser.py',228),
  ('factor -> var','factor',1,'p_factor_2','_parser.py',232),
  ('factor -> call','factor',1,'p_factor_3','_parser.py',236),
  ('factor -> NUMBER','factor',1,'p_factor_4','_parser.py',240),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','_parser.py',244),
  ('args -> args_list','args',1,'p_args','_parser.py',248),
  ('args -> empty','args',1,'p_args','_parser.py',249),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list_1','_parser.py',254),
  ('args_list -> expression','args_list',1,'p_args_list_2','_parser.py',258),
  ('empty -> <empty>','empty',0,'p_empty','_parser.py',262),
]
