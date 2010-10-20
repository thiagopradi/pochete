#coding: utf-8
import os

import ply.lex as lex
from ply.lex import TOKEN

palavras_reservadas = {'and':'AND', 'def':'DEF', 'elif':'ELIF','else':'ELSE',
		'false':'FALSE', 'if':'IF','input':'INPUT', 'not':'NOT', 'or':'OR', 'output':'OUTPUT', 'true':'TRUE', 'while':'WHILE'}

tokens = ['ID','RESERVADO','INTEIRO', 'BINARIO', 'OCTAL', 'HEXADECIMAL', 'REAL', 'LITERAL',
          'SIMBOLO', 'SIM_EQ', 'SIM_ATTR', 'SIM_POT', 'SIM_GE', 'SIM_LE', 'SIM_DIF'] + list(palavras_reservadas.values())

maiuscula = r'[A-Z]'
minuscula = r'[a-z]'
minuscula_digito = r'[0-9a-z]'
digito = r'[0-9]'
positivo = r'[1-9]'
aux_id = r'%s(%s %s?)*|%s(%s?%s)*%s?' % (maiuscula, minuscula_digito, maiuscula, minuscula, maiuscula,minuscula_digito, maiuscula)
aux_literal = r'"[^"]*"' + r"|'[^\r\n]*'"
new_line = (r"\r\n" if os.name == 'posix' else r"\r\n")

#t_SIMBOLO = r'\(|\)|\[|\]|,|;|:=|==|:|!=|<|<=|>|>=|\+|-|\*\*|\*|/|&|%'  
t_SIM_EQ = r'=='
t_SIM_ATTR = r':='
t_SIM_POT = r'\*\*'
t_SIM_GE = r'>='
t_SIM_LE = r'<='
t_SIM_DIF = r'=='
t_INTEIRO = r'0|%s%s*' % (positivo, digito)
t_ignore = ' \t\n'

literals = [';', ':', ',', '[', ']', '(', ')', '+', '-', '*', '/', '%']


def t_ignore_COMMENT(t):
  r'\#.*\n'
  t.lexer.lineno += 1
  pass

@TOKEN(aux_id)
def t_ID(t):
  r'aux_id'
  if t.value in palavras_reservadas:
    t.type = palavras_reservadas.get(t.value, 'ID')
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
  t.lexer.lineno += len(t.value.split(os.linesep)) - 1
  t.value = t.value.replace(os.linesep, r"\n")
  
  return t

def t_error(t):
  if(t.value.strip() and t.value.strip()[0] in ['"', "'"]):
    raise Exception(u"Erro na linha %s - constante literal não finalizada" % t.lexer.lineno)
  else:
    print t
    raise Exception(u"Erro na linha %s - %s - símbolo inválido" % (t.lexer.lineno, t.value[0]))
  
  
@TOKEN(new_line)
def t_newline(t):
  r'new_line'
  t.lexer.lineno += 1
  
def lexer():
  return lex.lex()
