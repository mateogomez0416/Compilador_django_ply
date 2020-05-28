import ply.yacc as yacc
from compiler.cp._lexer import tokens,lexer

import sys
import os
VERBOSE = 1
	

def p_program(p):
	'program : declaration_list'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" program")
	mensaje2.close()
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list declaration'
	
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" declaration list1")   
	mensaje2.close()
	mensaje2.close()
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" declaration list 2")
	mensaje2.close()
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" declaration")
	mensaje2.close()
	pass

def p_var_declaration_1(p):
	'var_declaration : type_specifier ID SEMICOLON'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" var declaration")
	mensaje2.close()
	pass

def p_var_declaration_2(p):
	'var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" var declaration 2")
	mensaje2.close()
	pass


def p_var_declaration_3(p):
	'var_declaration : type_specifier ID COMMA ID SEMICOLON'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" var declaration 3")
	mensaje2.close()
	pass




#---------------------------------------- 
#       TIPOS DE DATOS

def p_type_specifier_1(p):
	'type_specifier : E'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" type specifer1")
	mensaje2.close()
	pass

def p_type_specifier_2(p):
	'type_specifier : S'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" type specifer2")
	mensaje2.close()
	pass

def p_type_specifier_3(p):
	'type_specifier : F'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" type specifer3")
	mensaje2.close()
	pass
#----------------------------------------






def p_fun_declaration(p):
	'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" fun_declaration")
	mensaje2.close()
	pass


def p_params_1(p):
	'params : param_list'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params_1")
	mensaje2.close()
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params_list1")
	mensaje2.close()
	pass

def p_param_list_2(p):
	'param_list : param'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params_list2")
	mensaje2.close()
	pass

def p_param_list_3(p):
	'param_list : empty'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params_list3")
	mensaje2.close()
	pass

def p_param_1(p):
	'param : type_specifier ID'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params1")
	mensaje2.close()
	pass

def p_param_2(p):
	'param : type_specifier ID LBRACKET RBRACKET'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" params_2")
	mensaje2.close()
	pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" compount_stmt")
	mensaje2.close()
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" local_declarations_1")
	mensaje2.close()
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" local_declarations_2")
	mensaje2.close()
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" statement_list_1")
	mensaje2.close()
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" statement_list_2")	
	mensaje2.close()
	pass

#-----------------------------------
#          CONDICIONALES

def p_selection_stmt_1(p):
	'selection_stmt : SI LPAREN expression RPAREN statement'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" selection_stmt_1")
	mensaje2.close()
	pass

def p_selection_stmt_2(p):
	'selection_stmt : SI LPAREN expression RPAREN statement SINO statement'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" selection_stmt_2")
	mensaje2.close()
	pass


#-----------------------------------
#          ITERADORES

def p_iteration_stmt_1(p):
	'iteration_stmt : MQ LPAREN expression RPAREN statement'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" iteration_stmt_1")
	mensaje2.close()
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : H  statement  MQ LPAREN expression RPAREN'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" iteration_stmt_2")
	mensaje2.close()
	pass


def p_iteration_stmt_3(p):
	'iteration_stmt : for LPAREN ID EQUAL NUMBER SEMICOLON ID relop NUMBER SEMICOLON ID addop addop RPAREN statement'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" iteration_stmt_3")
	mensaje2.close()
	pass

#-----------------------------------

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				
	'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" statement")
	mensaje2.close()
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" expression_stmt_1")
	mensaje2.close()
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" expression_stmt_2")
	mensaje2.close()
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" expression_1")
	mensaje2.close()
	pass

def p_expression_2(p):
	'expression : simple_expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" expression_2")
	mensaje2.close()
	pass

def p_var_1(p):
	'var : ID'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" var_1")
	mensaje2.close()
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" var_2")
	mensaje2.close()
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" simple_expression_1")
	mensaje2.close()
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" simple_expression_2")
	mensaje2.close()
	pass

def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| AND
			| OR
	'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" relop")
	mensaje2.close()
	pass

def p_additive_expression_1(p):
	'additive_expression : additive_expression addop term'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" additive_expression_1")
	mensaje2.close()
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" additive_expression_2")
	mensaje2.close()
	pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" addop")
	mensaje2.close()
	pass

def p_term_1(p):
	'term : term mulop factor'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" term 1")
	mensaje2.close()
	pass

def p_term_2(p):
	'term : factor'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" term 2")
	mensaje2.close()
	pass

def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	            | POW
   	            | MODULO

	'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" mulop")
	mensaje2.close()
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" factor 1")
	mensaje2.close()
	pass

def p_factor_2(p):
	'factor : var'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" factor 2")

	mensaje2.close()
	pass

def p_factor_3(p):
	'factor : call'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" factor 3")

	mensaje2.close()
	pass

def p_factor_4(p):
	'factor : NUMBER'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" factor 4")
 
	mensaje2.close()
	pass

def p_call(p):
	'call : ID LPAREN args RPAREN'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" call")

	mensaje2.close()
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" args")
	mensaje2.close()
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" args_list_1")
	mensaje2.close()
	pass

def p_args_list_2(p):
	'args_list : expression'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" args_list_2")
	mensaje2.close()
	pass

def p_empty(p):
	'empty :'
	mensaje2=open("parsePasos.outt","a")
	mensaje2.write(" empty")
	mensaje2.close()
	pass

def p_error(p):

	
	if VERBOSE:
		
		if p is not None:

			mensaje = open("parseMs.outt","w")
			mensaje.write("Token inesperado  "+str(p.value))
			#+" en la linea: "+str(mini_c_lexer.lexer.lineno)
			mensaje.close()

		else:
			mensaje = open("parseMs.outt","w")
			mensaje.write("Error de sintaxis... ")
			mensaje.close()

	else:
		mensaje = open("parseMs.outt","w")
		mensaje.write("Error de sintaxis... ")
		mensaje.close()

		
		

parser = yacc.yacc()

if __name__ == '__main__':

	data = ''' 
	         /variables/ 
             E a,c; 


             /Mi Programa/
            
             E main(){
       
   



            }
               
	''' 



	parser.parse(data, tracking=True)
	

