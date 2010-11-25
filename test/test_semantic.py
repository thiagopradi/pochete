# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, pochete_parser, SemanticTools

class TestSemantic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
    
    def test_semantic_action_2_with_success(self):
      pochete_parser(u"def teste : \n [ abc := 0; input(abc);  ]", lexer())
      self.assertTrue(SemanticTools.defined_variables.get('teste'))
    
    def test_semantic_error_with_input(self):
      try: 
        pochete_parser(u"def teste : \n [ input(lado);  ]", lexer())
        raise Exception("Error")
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - identificador (lado) não declarado", e.message)

    def test_semantic_success_with_input(self):
      pochete_parser(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())