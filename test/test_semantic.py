# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, SemanticTools

class TestSemantic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()
    
    def test_semantic_action_1_with_success(self):
      pass
    
    def test_semantic_action_3_with_success(self):
      pass
    
    def test_semantic_action_2_with_success(self):
      parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())
      self.assertTrue(SemanticTools.defined_variables.get('teste'))
    
    def test_semantic_action_2_with_fail(self):
      try: 
        parser.parse(u"def teste : \n [ teste := 0; input(teste);  ]", lexer())
        raise Exception("Error")
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - identificador teste já declarado anteriormente", e.message)

    # TODO
    # def test_semantic_error_with_input(self):
    #   try: 
    #     parser.parse(u"def teste : \n [ input(lado);  ]", lexer())
    #     raise Exception("Error")
    #   except Exception, e:
    #     self.assertEqual(u"Erro na linha 2 - identificador (lado) não declarado", e.message)

    def test_semantic_success_with_input(self):
      parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())
