# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, SemanticTools

class TestLexer(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()
      
      
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
        
    def test_empty_string_parse(self):
      try: 
        parser.parse(u"", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado def", e.message)
        
    