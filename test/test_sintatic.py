# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, SemanticTools

class TestSintatic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()

    def test_sintatic_exception_with_line_number(self):
      try: 
        parser.parse(u"def teste : \n := a := 1; \n b := 2;  ]", lexer())
      except Exception, e:
        pass
      
      try: 
        parser.parse(u"def teste : \n := a := 1; \n b := 2;  ]", lexer())
        raise Exception("Oi")
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - encontrado :=, esperado [", e.message)

    def test_sintatic_exception(self):
      try: 
        parser.parse(u"def teste ab [ c := 1; \n d := 2;  ]", lexer())
      except Exception, e:
        pass
      try: 
        parser.parse(u"def teste ab [ c := 1; \n d := 2;  ]", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado ab, esperado :", e.message)
        
    def test_with_only_def(self):
      try: 
        parser.parse(u"def", lexer())
      except Exception, e:
        pass
      try: 
        parser.parse(u"def", lexer())
      except Exception, e:      
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado identificador", e.message)  
    
    def test_with_def_and_identifier(self):
      try: 
        parser.parse(u"def abc", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado ':'", e.message)  
    
    def test_with_def_and_identifier_and_symbol(self):
      try: 
        parser.parse(u"def abc : ", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado '['", e.message)  

    def test_with_def_and_identifier_and_symbol_other(self):
      try: 
        parser.parse(u"def abc : [", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado comando", e.message)  
    
    def test_with_def_and_identifier_and_symbol_other(self):
      try: 
        parser.parse(u"def abc : [ a := a+1;", lexer())
      except Exception, e:
        self.assertEqual(u"Erro na linha 1 - encontrado EOF, esperado ]", e.message)  
    
    
         
