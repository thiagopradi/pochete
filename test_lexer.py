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
      
    def test_exception_new_line_with_rn(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \r\n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - ? - símbolo inválido", e.message)

    def test_exception_new_line_with_n(self):
      try: 
        parser.parse(u"def abc : [ a := 1; \n a := 2; ? ]", self.var_lex)
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - ? - símbolo inválido", e.message)    
      

if __name__ == '__main__':
    unittest.main()