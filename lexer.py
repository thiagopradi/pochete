import ply.lex as lex
from ply.lex import TOKEN

tokens = ('ID','RESERVADO','INTEIRO', 'BINARIO', 'OCTAL', 'HEXADECIMAL', 'REAL', 'LITERAL', 'SIMBOLO')

maiuscula = r'[A-Z]'
minuscula = r'[a-z]'
minuscula_digito = r'[0-9a-z]'
digito = r'[0-9]'
positivo = r'[1-9]'
aux_id = r'%s(%s %s?)*|%s(%s?%s)*%s?' % (maiuscula, minuscula_digito, maiuscula, minuscula, maiuscula,minuscula_digito, maiuscula)
aux_literal = r"'[^\n']*'|" + r'\"[^"]"'

t_SIMBOLO = r'\(|\)|\[|\]|,|;|:=|==|:|!=|<|<=|>|>=|\+|-|\*\*|\*|/|&|%'  
t_ignore_COMMENT = r'\#.*'
t_INTEIRO = r'0|%s%s*' % (positivo, digito)
t_ignore = ' \t'

@TOKEN(aux_id)
def t_ID(t):
  r'aux_id'
  palavras_reservadas = ['and', 'def', 'elif','else','false', 'if','input', 'not', 'or', 'output', 'true', 'while']
  if t.value in palavras_reservadas:
    t.type = 'RESERVADO'
  
  return t

def t_BINARIO(t):
  r'0(b|B)(0|1)+'
  return t
  
def t_OCTAL(t):
  r"0(o|O)[0-7]+"
  return t

def t_HEXADECIMAL(t):
  r"0(x|X)[0-9a-fA-F]+"
  return t
  
def t_REAL(t):
  r"(0|[1-9][0-9]*)\.(0|[0-9]*[1-9])"
  return t

@TOKEN(aux_literal)
def t_LITERAL(t):
  r'aux_literal'
  return t

lexer = lex.lex()

lexer.input(' Pfda "fdipoasjfpodsa" fdasjipfpoasd and 0.0 0.1 0.2 3.2132 fjdpasjfd or 0x932AFfd89 jfdopajifd *** 0o31278 0o8 ::= 0b001 0B111 111 01 #fjdpoajfpoijdasofjas')


for tok in lexer:
  print tok
