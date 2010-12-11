# coding: utf-8
import ply.yacc as yacc
from lexer import tokens, lexer
  
class SemanticTools:
    defined_variables = {}
    main_identifier = ""
    code = []
    alloc = []
    program_name = "teste"
    symbol_table = {}
    code_op = []
    operation = False
    token = None
    
    @classmethod
    def reset(cls):
        cls.defined_variables = {}
        cls.context = ""
        cls.code = []
        cls.alloc = []
        cls.token = None
        cls.symbol_table = {}
        cls.code_op = []

# ACTION3 está implementada aqui
def p_programa(p):
    """programa : DEF ID action2 ':' '[' listacmd ']'
    | empty """
    if len(p) <= 2:
      raise Exception(u"Erro na linha %s - encontrado %s, esperado %s" % (1, 'EOF', 'def'))
    alloc_string = ''.join(SemanticTools.alloc)
    SemanticTools.code.insert(1, alloc_string)
    SemanticTools.code.append("""
        ret
        }
        }
      """) 
    
def p_action2(p):
    "action2 :"
    SemanticTools.main_identifier = p[-1]
    SemanticTools.code.append(""".assembly extern mscorlib{}
    .assembly %s{}
    .module %s.exe
    .class public %s
    {
    .method public static void principal ()
    {
    .entrypoint""" % (SemanticTools.program_name, SemanticTools.program_name, SemanticTools.program_name))
    
    
def p_programa_error(p):
    """programa : DEF ID action2 error '[' listacmd ']'  
    | DEF ID action2 ':' error listacmd ']' 
    | DEF ID action2 ':' '[' listacmd error
    | DEF
    | DEF ID
    | DEF ID action2 ':'
    | DEF ID action2 ':' '['
    | DEF ID action2 ':' '[' listacmd"""
    errors = {7: "']'", 6:"comando", 5:"'['", 3:"':'", 2:'identificador'}
    if errors.get(len(p)):
      raise Exception(u"Erro na linha %s - encontrado %s, esperado %s" % (p.lineno(1), 'EOF',errors.get(len(p))))        
    _generateError(p, {1:"def",4:":", 5:"[", 7:']'})
        
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

# ACTION5 is here
def p_listaidenti(p):
    "listaidenti : ID listaindenti1"    
    if SemanticTools.main_identifier == p[1]:
      raise Exception(u"Erro na linha %s - identificador %s já declarado anteriormente" % (p.lineno(1), p[1]))
    SemanticTools.defined_variables[p[1]] = True
    
def p_listaindenti1(p):
    """listaindenti1 : empty
                     | ',' listaidenti"""    

def p_listaexp(p):
    "listaexp : expressao listaexp1"
    pass
    
def p_listaexp1(p):
    """listaexp1 : ',' action7 listaexp
                 | empty action7 """

def p_action7(p):
    "action7 : "
    # Identificador x = (Identificador) tabelaSimbolos.get(token.getLexeme());
    #     if (x == null) {
    #         throw new SemanticError("identificador ( " + token.getLexeme() + " ) não declarado");
    #     }
    #     arrayCodigo.add("        ldloc " + token.getLexeme());
    #     if (x.getTipo().equals("inteira") || x.getTipo().equals("hexadecimal") || x.getTipo().equals("octal") || x.getTipo().equals("binária")) {
    #         arrayCodigo.add("        call void [mscorlib]System.Console::Write(int32)");
    #     } else if (x.getTipo().equals("real")) {
    #         arrayCodigo.add("        call void [mscorlib]System.Console::Write(float32)");
    #     } else if (x.getTipo().equals("literal")) {
    #         arrayCodigo.add("        call void [mscorlib]System.Console::Write(string)");
    #     }

def p_listaexp1_error(t):
    """listaexp1 : error action7 listaexp"""
    _generateError(t, {1:","})
    
def p_cmdatribui(p):
    "cmdatribui : listaidenti SIM_ATTR expressao action4 ';'"

def p_action4(p):
    "action4 : "
    newVariable = False
    for key, value in SemanticTools.defined_variables.iteritems():
        if not key in SemanticTools.symbol_table.keys():
          newVariable = True
          SemanticTools.symbol_table[key] = value
        if value in ["integer", "octal", "hexa", "binary"]:
          if newVariable:
            SemanticTools.alloc.append("        .locals init (int32 " + key + ")")
          if not SemanticTools.operation:
            if value == "integer":
              SemanticTools.code.append("        ldc.i4 "+ SemanticTools.token.value)
            elif value == "binary":
              SemanticTools.code.append("        ldc.i4 "+ str(int(SemanticTools.token.value, 2)))
            elif value == "hexa":
              SemanticTools.code.append("        ldc.i4 "+ str(int(SemanticTools.token.value, 16)))
            elif value == "octal":
              SemanticTools.code.append("        ldc.i4 "+ str(int(SemanticTools.token.value, 8)))
              
          SemanticTools.code.append("       stloc "+ key)
        elif value == "real":
          if newVariable:
            SemanticTools.alloc.append("        .locals init (float32 " + key + ")")
          if not SemanticTools.operation:
             SemanticTools.code.append("        ldc.r4  "+ SemanticTools.token.value)
        elif value == "literal":
          if newVariable:
            SemanticTools.alloc.append("        .locals init (string " + key + ")")
          if not SemanticTools.operation:
            SemanticTools.code.append("        ldstr "+ SemanticTools.token.value)
          SemanticTools.code.append("        stloc " + key)
        else:
          if value == "bool":
            if newVariable:
              SemanticTools.alloc.append("        .locals init (int32 " + key + ")")
            if not SemanticTools.operation:
              if SemanticTools.token.value == "true":
                integer = '1'
              else:
                integer = '0'
              SemanticTools.code.append("        ldc.i4  " + integer)
            SemanticTools.code.append("        stloc " + key)
          
    SemanticTools.defined_variables = {}
    SemanticTools.code_op = []
    SemanticTools.operation = False

def p_cmdentrada(p):
    "cmdentrada : INPUT '(' listaidenti action6 ')' ';'"
    for key in SemanticTools.defined_variables.keys():
      if not SemanticTools.symbol_table.get(key):
        raise Exception(u"Erro na linha %s - identificador %s não declarado" % (p.lineno(1), key))
      id_type = SemanticTools.symbol_table.get(key)
      SemanticTools.code.append('call string [mscorlib]System.Console::ReadLine()')
      if id_type in ['integer', 'hexa', 'binary', 'octal']:
        SemanticTools.code.append("call int32 [mscorlib]System.Int32::Parse(string)")
        SemanticTools.code.append("stloc "+ key)
      elif id_type == 'real':
        SemanticTools.code.append("call float32 [mscorlib]System.Float32::Parse(string)")
        SemanticTools.code.append("stloc "+ key)
      elif id_type == "literal":
        SemanticTools.code.append("stloc "+ key)
                
def p_action6(p):
    "action6 : "

def p_cmdentrada_error(t):
    """cmdentrada : INPUT '(' listaidenti action6 error ';' 
    | INPUT error listaidenti action6 ')' ';' 
    | INPUT '(' listaidenti  action6 ')' error """
    _generateError(t, {2:"(",4:")", 5:";"})

def p_cmdsaida(p):
    "cmdsaida : OUTPUT '(' listaexp ')' ';'"
    for key in SemanticTools.defined_variables.keys():
      if not SemanticTools.symbol_table.get(key) and SemanticTools.defined_variables.get(key) == 'id':
        raise Exception(u"Erro na linha %s - identificador %s não declarado" % (p.lineno(1), key))
      SemanticTools.code.append("        ldloc "+ key)
      id_type = SemanticTools.symbol_table.get(key)
      if id_type in ['integer', 'hexa', 'binary', 'octal']:
        SemanticTools.code.append("        call void [mscorlib]System.Console::Write(int32)")
      elif id_type == 'real':
        SemanticTools.code.append("        call void [mscorlib]System.Console::Write(float32)")
      elif id_type == "literal":
        SemanticTools.code.append("        call void [mscorlib]System.Console::Write(string)")
    
def p_cmdsaida_error(t):
    """cmdsaida : OUTPUT '(' listaexp error ';' 
    | OUTPUT error listaexp ')' ';' 
    | OUTPUT '(' listaexp ')' error    """
    _generateError(t, {2:"(",4:")", 5:";"})
        
def p_cmdselecao(p):
    "cmdselecao : IF expressao action8 ':' '[' listacmd ']' action9 elif else ';'"
    pass

def p_action8(p):
    "action8 : "

def p_action9(p):
    "action9 : "
    
def p_cmdselecao_error(t):
    """cmdselecao : IF expressao action8 error '[' listacmd ']' action9 elif else ';'
    | IF expressao action8 ':' error listacmd ']' action9 elif else ';'
    | IF expressao action8 ':' '[' listacmd error action9 elif else ';' 
    | IF expressao action8 ':' '[' listacmd ']' action9 elif else error"""
    _generateError(t, {3:":", 4:"[", 6:']', 9:';'})

def p_elif(p):
    """elif : empty 
            | action10 ELIF expressao action11 ':' '[' listacmd ']' elif"""
    pass

def p_action10(p):
    "action10 : "

def p_action11(p):
    "action11 : "
    
def p_elif_error(t):
  """elif : action10 ELIF expressao action11 error '[' listacmd ']' elif
     | action10 ELIF expressao action11 ':' error listacmd ']' elif
     | action10 ELIF expressao action11 ':' '[' listacmd error elif"""
  _generateError(t, {3:":", 4:"[", 6:']'})
  
def p_else(p):
    """else : empty
            | action12 ELSE ':' '[' listacmd ']'"""
    pass

def p_action12(p): 
    "action12 : "

def p_else_error(t):
    """else : ELSE error '[' listacmd ']' 
    | ELSE ':' error listacmd ']' 
    | ELSE ':' '[' listacmd error """
    _generateError(t, {2:":", 3:"[", 5:']'})
  
def p_cmdrepeticao(p):
    "cmdrepeticao : WHILE action13 expressao action14 ':' '[' listacmd ']' action15 else ';'"
    pass

def p_action13(p): 
    "action13 : "

def p_action14(p): 
    "action14 : "

def p_action15(p): 
    "action15 : "

def p_cmdrepeticao_error(t):
    """cmdrepeticao : WHILE action13 expressao action14 error '[' listacmd ']' action15 else ';' 
    | WHILE action13 expressao action14 ':' error listacmd ']' action15 else ';'
    | WHILE action13 expressao action14 ':' '[' listacmd error action15 else ';'
    | WHILE action13 expressao action14 ':' '[' listacmd ']' action15 else error"""
    _generateError(t, {3:":", 4:"[", 6:']', 8:';'})
  
def p_expressao(p):
    "expressao : valor expressao1"

def p_expressao1(p):
    """expressao1 : empty
                | OR valor action_16 expressao1
                | AND valor action_17 expressao1 """
    pass

def p_action_16(p):
    "action_16 : "
    SemanticTools.code.append("        or")
    
def p_action_17(p):
    "action_17 : "
    SemanticTools.code.append("        and")

def p_expressao1_error(t):
    """expressao1 : error valor expressao1"""
    _generateError(t, {1:"Expressão"})

def p_valor(p):
    """valor : relacional
           | TRUE action18
           | FALSE action19
           | NOT valor action20"""
           
def p_action_18(p):
    "action18 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "bool"
    SemanticTools.token = p.stack[-1]

def p_action_19(p):
    "action19 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "bool"
    SemanticTools.token = p.stack[-1]

def p_action_20(p):
    "action20 : "

def p_relacional(p):
    "relacional : aritmetica relacional1"
    pass

def p_relacional1(p):
    """relacional1 : operador action21 aritmetica action22
                 | empty"""

def p_action_21(p):
    "action21 : "

def p_action_22(p):
    "action22 : "

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
    
    
def p_aritmetica1(p):
    """aritmetica1 : empty
                   | '+' termo aritmetica1 p_action23
                   | '-' termo aritmetica1 p_action24 """
    
def p_termo(p):
    "termo : fator termo1"
    pass

def p_termo1(p):
    """termo1 : empty
              | '*' fator termo1 p_action25
              | '/' fator termo1 p_action26
              | '%' fator termo1 p_action27 """
    pass

def p_fator(p):
    "fator : elemento fator1"
    pass
    
def p_fator1(p):
    """fator1 : empty
              | SIM_POT elemento action28 fator1"""


def p_action28(p):
    "action28 : "

def p_elemento(p):
    """elemento : ID action29
                | INTEIRO action30
                | BINARIO action31
                | OCTAL action32
                | HEXADECIMAL action33
                | REAL action34
                | LITERAL action35
                | '(' expressao ')'
                | '+' elemento
                | '-' elemento action36"""
    
    
def p_action29(p):
    "action29 : "
    SemanticTools.defined_variables[p.stack[-1].value] = "id"
    SemanticTools.code_op.append("        ldloc " + p.stack[-1].value)
    SemanticTools.token = p.stack[-1]

def p_action30(p):
    "action30 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "integer"
    SemanticTools.token = p.stack[-1]

def p_action31(p):
    "action31 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "binary"
    SemanticTools.token = p.stack[-1]

def p_action32(p):
    "action32 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "octal"
    SemanticTools.token = p.stack[-1]

def p_action33(p):
    "action33 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "hexa"
    SemanticTools.token = p.stack[-1]

def p_action34(p):
    "action34 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "real"
    SemanticTools.token = p.stack[-1]

def p_action35(p):
    "action35 : "
    for key, value in SemanticTools.defined_variables.iteritems():
      SemanticTools.defined_variables[key] = "literal"
    SemanticTools.token = p.stack[-1]

def p_action36(p):
    "action36 : "
    SemanticTools.code += "\n        neg"

def p_action23(p):
  "p_action23 : "
  SemanticTools.code += '\n'.join(SemanticTools.code_op)
  print SemanticTools.defined_variables
  SemanticTools.code += "\n add"
  SemanticTools.operation = True
  
def p_action24(p):
  "p_action24 : "
  SemanticTools.code += "\n sub"
  
def p_action25(p):
  "p_action25 : "
  SemanticTools.code += "\n mul"

def p_action26(p):
  "p_action26 : "
  SemanticTools.code += "\n div"

def p_action27(p):
  "p_action27 : "
  SemanticTools.code += "\n rem"  

def p_error(p):
    raise Exception(u"Erro na linha %s - encontrado %s, esperado construção sintática válida" % (p.lineno, p.value))

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
