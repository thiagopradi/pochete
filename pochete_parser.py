# coding: utf-8
import ply.yacc as yacc
from lexer import tokens, lexer

class CompilerFlag:
  bool = False
  
class SemanticTools:
  defined_variables = {}
  context = ""
  # The LLVM module, which holds all the IR code.
  #g_llvm_module = Module.new('Pochete Module')
  # The LLVM instruction builder. Created whenever a new function is entered.
  #g_llvm_builder = None
  # A dictionary that keeps track of which values are defined in the current scope
  # and what their LLVM representation is.
  #g_named_values = {}

def p_programa(p):
    """programa : DEF ID ':' '[' listacmd ']' 
    | empty"""
    if len(p) < 2:
      raise Exception(u"Erro na linha %s - encontrado %s, esperado %s" % (1, 'EOF', 'def'))

def p_programa_error(t):
    """programa : DEF ID error '[' listacmd ']' 
    | DEF ID ':' error listacmd ']' 
    | DEF ID ':' '[' listacmd error """
    _generateError(t, {1:"def",3:":", 4:"[", 6:']'})
        
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
    if(SemanticTools.context == 'atribui'):
      SemanticTools.defined_variables[p[1]] = True
      SemanticTools.context = ""
    
    if(p.stack[len(p.stack)-2].value == 'input' and not SemanticTools.defined_variables.get(p[1])):
      raise Exception(u"Erro na linha %s - identificador (%s) não declarado" % (p.lineno(1), p[1]))    
    
    
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

def p_listaexp1_error(t):
    """listaexp1 : error listaexp"""
    _generateError(t, {1:","})
    
def p_cmdatribui(p):
    "cmdatribui : listaidenti SIM_ATTR expressao ';'"
    if(p[2] == ":="):
      SemanticTools.context = "atribui"
    
def p_cmdentrada(p):
    "cmdentrada : INPUT '(' listaidenti ')' ';'"
    
def p_cmdentrada_error(t):
    """cmdentrada : INPUT '(' listaidenti error ';' 
    | INPUT error listaidenti ')' ';' 
    | INPUT '(' listaidenti ')' error """
    _generateError(t, {2:"(",4:")", 5:";"})

def p_cmdsaida(p):
    "cmdsaida : OUTPUT '(' listaexp ')' ';'"
    pass

def p_cmdsaida_error(t):
    """cmdsaida : OUTPUT '(' listaexp error ';' 
    | OUTPUT error listaexp ')' ';' 
    | OUTPUT '(' listaexp ')' error    """
    _generateError(t, {2:"(",4:")", 5:";"})
        
def p_cmdselecao(p):
    "cmdselecao : IF expressao ':' '[' listacmd ']' elif else ';'"
    pass
    
def p_cmdselecao_error(t):
    """cmdselecao : IF expressao error '[' listacmd ']' elif else ';'
    | IF expressao ':' error listacmd ']' elif else ';'
    | IF expressao ':' '[' listacmd error elif else ';' 
    | IF expressao ':' '[' listacmd ']' elif else error """
    _generateError(t, {3:":", 4:"[", 6:']', 9:';'})

def p_elif(p):
    """elif : empty 
            | ELIF expressao ':' '[' listacmd ']' elif"""
    pass
    
def p_elif_error(t):
  """elif : ELIF expressao error '[' listacmd ']' elif
     | ELIF expressao ':' error listacmd ']' elif
     | ELIF expressao ':' '[' listacmd error elif"""
  _generateError(t, {3:":", 4:"[", 6:']'})
  
def p_else(p):
    """else : empty
            | ELSE ':' '[' listacmd ']'"""
    pass

def p_else_error(t):
  """else : ELSE error '[' listacmd ']' 
  | ELSE ':' error listacmd ']' 
  | ELSE ':' '[' listacmd error """
  _generateError(t, {2:":", 3:"[", 5:']'})
  
def p_cmdrepeticao(p):
    "cmdrepeticao : WHILE expressao ':' '[' listacmd ']' else ';'"
    pass

def p_cmdrepeticao_error(t):
  """cmdrepeticao : WHILE expressao error '[' listacmd ']' else ';' 
  | WHILE expressao ':' error listacmd ']' else ';'
  | WHILE expressao ':' '[' listacmd error else ';'
  | WHILE expressao ':' '[' listacmd ']' else error"""
  _generateError(t, {3:":", 4:"[", 6:']', 8:';'})
  
def p_expressao(p):
    "expressao : valor expressao1"
    pass

def p_expressao1(p):
    """expressao1 : empty
                | OR valor expressao1
                | AND valor expressao1"""
    pass

def p_expressao1_error(t):
    """expressao1 : error valor expressao1"""
    _generateError(t, {1:"Expressão"})

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
    
    
def p_error(t):
    if not CompilerFlag.bool:
      CompilerFlag.bool = True
      raise Exception(u"Erro na linha %s - encontrado %s, esperado %s" % (t.lineno, str(t), ''))
    
  
def _getTokenValue(t):
    if not t:
        return "EOF"
    else:
        if type(t) in [str, unicode]:
            return t
        else:
            return t.value
            
def _generateError(t, dictionary):
    for k, v in dictionary.items():
        if _getTokenValue(t[k]) != v:
            raise Exception(u"Erro na linha %s - encontrado %s, esperado %s" % (t.lineno(k), _getTokenValue(t[k]), v))
  
parser = yacc.yacc()