# coding: utf-8

import unittest
from lexer import lexer
from pochete_parser import parser

class TestLexer(unittest.TestCase):  
    def setUp(self):
      self.var_lex = lexer()
      
    def test_tokens(self):
      self.var_lex.input("a := 1")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "a")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, ":=")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "1")
      
    def test_new_line(self):
      self.var_lex.input("a := 1\na := 2")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "a")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, ":=")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "1")
      tok = self.var_lex.token()          
      self.assertEqual(tok.value, "a")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, ":=")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "2")
      
    def test_real(self):
      self.var_lex.input("1.0")
      self.assertEqual(self.var_lex.token().value, "1.0")

    def test_binary(self):
      self.var_lex.input("0b01")
      self.assertEqual(self.var_lex.token().value, "0b01")
    
    def test_octal(self):
      self.var_lex.input("0o00")
      self.assertEqual(self.var_lex.token().value, "0o00")
  
    def test_hexadecimal(self):
      self.var_lex.input("0x00")
      self.assertEqual(self.var_lex.token().value, "0x00")
      
    def test_exception_new_line_with_rn(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \r\n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - ? - símbolo inválido", e.message)
        
    def test_exception_new_line_with_rn_and_multiple_lines(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \r\n\r\n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 3 - ? - símbolo inválido", e.message)

    def test_exception_new_line_with_n(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - ? - símbolo inválido", e.message)    

    def test_exception_new_line_with_n_and_multiple_lines(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \n \n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 3 - ? - símbolo inválido", e.message)    

    def test_sintatic_exception(self):
      try: 
        parser.parse(u"def teste a [ a := 1; \n a := 2;  ]", lexer())
      except Exception, e:
        pass
      try: 
        parser.parse(u"def teste a [ a := 1; \n a := 2;  ]", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado a, esperado :", e.message)
    
    def test_sintatic_exception_with_line_number(self):
      try: 
        parser.parse(u"def teste : \n := a := 1; \n a := 2;  ]", lexer())
      except Exception, e:
        pass
      try: 
        parser.parse(u"def teste : \n := a := 1; \n a := 2;  ]", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - encontrado :=, esperado [", e.message)

if __name__ == '__main__':
    unittest.main()