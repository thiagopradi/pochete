# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser

class TestSemantic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()

    def test_semantic_error_with_input(self):
      try: 
        parser.parse(u"def teste : \n [ input(lado);  ]", lexer())
        raise Exception("Error")
      except Exception, e:
        self.assertEqual(u"Erro na linha 2 - identificador (lado) não declarado", e.message)

    def test_semantic_success_with_input(self):
      parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())