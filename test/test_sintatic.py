# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser

class TestSintatic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()
      
      
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