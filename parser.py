# coding: utf-8
import ply.yacc as yacc
from lexer import tokens, lexer

def p_programa(p):
    "programa : DEF ID ':' '[' listacmd ']'"
    pass

def p_empty(p):
    "empty :"
    pass
    
def p_listacmd(p):
    "listacmd : comando listacmd1"
    pass
    
def p_listacmd1(p):
    """listacmd1 : empty 
               | listacmd"""
    pass
    
def p_comando(p):
    """comando : cmdatribui
               | cmdentrada
               | cmdsaida
               | cmdselecao
               | cmdrepeticao"""
    pass

def p_listaidenti(p):
    "listaidenti : ID listaindenti1"
    pass

def p_listaindenti1(p):
    """listaindenti1 : empty
                     | ',' listaidenti"""
    pass

def p_listaexp(p):
    "listaexp : expressao listaexp1"
    pass

def p_listaexp1(p):
    """listaexp1 : ',' listaexp
                 | empty """
    pass

def p_cmdatribui(p):
    "cmdatribui : listaidenti SIM_ATTR expressao ';'"
    pass

def p_cmdentrada(p):
    "cmdentrada : INPUT '(' listaidenti ')' ';'"
    pass

def p_cmdsaida(p):
    "cmdsaida : OUTPUT '(' listaexp ')' ';'"
    pass

def p_cmdselecao(p):
    "cmdselecao : IF expressao ':' '[' listacmd ']' elif else ';'"
    pass
    
def p_elif(p):
    """elif : empty 
            | ELIF expressao ':' '[' listacmd ']' elif"""
    pass

def p_else(p):
    """else : empty
            | ELSE ':' '[' listacmd ']'"""
    pass

def p_cmdrepeticao(p):
    "cmdrepeticao : WHILE expressao ':' '[' listacmd ']' else ';'"
    pass

def p_expressao(p):
    "expressao : valor expressao1"
    pass

def p_expressao1(p):
    """expressao1 : empty
                | OR valor expressao1
                | AND valor expressao1"""
    pass

def p_valor(p):
    """valor : relacional
           | TRUE
           | FALSE
           | NOT valor"""
    pass

def p_relacional(p):
    "relacional : aritmetica relacional1"
    pass

def p_relacional1(p):
    """relacional1 : operador aritmetica
                 | empty"""
    pass

def p_operador(p):
    """operador : SIM_EQ
              | SIM_DIF
              | '<'
              | SIM_LE
              | '>'
              | SIM_GE"""
    pass

def p_aritmetica(p):
    "aritmetica : termo aritmetica1"
    pass

def p_aritmetica1(p):
    """aritmetica1 : empty
                   | '+' termo aritmetica1
                   | '-' termo aritmetica1"""
    pass

def p_termo(p):
    "termo : fator termo1"
    pass

def p_termo1(p):
    """termo1 : empty
              | '*' fator termo1
              | '/' fator termo1
              | '%' fator termo1"""
    pass

def p_fator(p):
    "fator : elemento fator1"
    pass

def p_fator1(p):
    """fator1 : empty
              | SIM_POT elemento fator1"""
    pass

def p_elemento(p):
    """elemento : ID
                | INTEIRO
                | REAL
                | LITERAL
                | '(' expressao ')'
                | '+' elemento
                | '-' elemento"""
    pass

parser = yacc.yacc()
s = """def teste: [
		output(1);
		input(a, b);
		output(a);
		y := 1 + 2;
		ba := 32 * 33;
		if a : [
		  ba := ba + 3;
		] elif a : [
		  ba := ba+3;
		] else: [
		  ba := ba+3;
		];
		
		while a: [
		  ba:= ba+3;
		] else : [
		  ba := ba+3;
		];
		
		#else: [
		#  bff := ff+2;
		#];
	]"""
print parser.parse(s, lexer=lexer())
