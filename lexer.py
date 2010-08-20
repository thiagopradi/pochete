import ply.lex as lex

tokens = ('NOME','NUMERO','DATA')

maiuscula = r'[A-Z]'
minuscula = r'[a-z]'
conectivo = r'(de|da|dos)'
digito = r'[0-9]'
first_data_digit = r'[1-2]'
second_data_digit = r'[0-9]'
teste = r'0[1-9]'


t_NOME = r'%s%s+(\s(%s\s)?%s%s+)+' %(maiuscula, minuscula, conectivo, maiuscula, minuscula)
t_NUMERO = r'10(,00?)|%s(,%s%s?)?' %(digito, digito, digito)
t_DATA = r'(%s%s|30|31|%s)/(0%s|10|11|12)/(%s)' %(first_data_digit, second_data_digit, teste, second_data_digit, (second_data_digit*4))

t_ignore = ' '

lexer = lex.lex()
lexer.input('12/12/2009')

for tok in lexer:
  print tok
