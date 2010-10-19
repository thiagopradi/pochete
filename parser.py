import ply.yacc as yacc
from lexer import tokens, lexer

def p_programa(p):
    'def identificador : [<lista de comandos>]'
    pass

def p_element(p):
    ' <elemento> ::= identificador | constante_inteira | constante_real | constante_literal | ( <expressão> ) | + <elemento> | - <elemento>'
    pass

def p_fator1(p):
    ' <fator1> ::=  | ** <elemento> <fator1>'
    pass

def p_fator(p):
    ' <fator> ::= <elemento> <fator1>'
    pass

def p_termo1(p):
    ' <termo1> ::=  | * <fator> <termo1> | / <fator> <termo1> | % <fator> <termo1>'
    pass

def p_termo(p):
    ' <termo> ::= <fator> <termo1>'
    pass

def p_aritmetica1(p):
    ' <aritmetica1> ::=  | + <termo> <aritmética1> | - <termo> <aritmética1>'
    pass

def p_aritmetica(p):
    ' <aritmetica> ::= <termo> <aritmética1>'
    pass

def p_operador(p):
    ' <operador> ::= == | != | < | <= | > | >='
    pass

def p_relacional1(p):
    ' <relacional1> ::= <operador> <aritmética> | '
    pass

def p_relacional(p):
    ' <relacional> ::= <aritmética> <relacional1>'
    pass

def p_valor(p):
    ' <valor> ::= <relacional> | true | false | not <valor>'
    pass

def p_expressao1(p):
    ' <expressao1> ::=  | or <valor> <expressão1> | and <valor> <expressão1>'
    pass

def p_expressao(p):
    ' <expressao> ::= <valor> <expressão1>'
    pass

def p_cmdrepeticao(p):
    ' <cmdrepeticao> ::= while <expressão> : [ <lista de comandos>] <else>;'
    pass

def p_else(p):
    ' <else> ::=  | else: [ <lista de comandos> ]'
    pass

def p_elif(p):
    ' <elif> ::=  | elif <expressão> : [ <lista de comandos> ] <elif>'
    pass

def p_cmdselecao(p):
    ' <cmdselecao> ::= if <expressão> : [ <lista de comandos>] <elif> <else>;'
    pass

def p_cmdsaida(p):
    ' <cmdsaida> ::= output( <listaexp> );'
    pass

def p_cmdentrada(p):
    ' <cmdentrada> ::= input( <lista de identificadores> );'
    pass

def p_cmdatribui(p):
    ' <cmdatribui> ::= <lista de identificadores> := <expressão>;'
    pass

def p_listaexp1(p):
    ' <listaexp1> ::= , <listaexp> | '
    pass

def p_listaexp(p):
    ' <listaexp> ::= <expressão> <listaexp1>'
    pass

def p_listaindenti1(p):
    ' <listaindenti1> ::=  | <lista de identificadores>'
    pass

def p_listaidenti(p):
    ' <listaidenti> ::= identificador <listaindenti1>'
    pass

def p_comando(p):
    ' <comando> ::= <cmdatribui> | <cmdentrada> | <cmdsaida> | <cmdselecao> | <cmdrepeticao>'
    pass

def p_listacmd1(p):
    ' <listacmd1> ::=  | <lista de comandos>'
    pass

def p_listacmd(p):
    ' <listacmd> ::= <comando> <listacmd1>'
    pass

def p_teste(p):
    ' <programa> ::= def identificador : [<listacmd>]'
    pass



