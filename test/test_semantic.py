# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, SemanticTools

class TestSemantic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()
    
    def assertParserError(self, parse_string, error):
        self.assertRaisesRegexp(Exception, error, parser.parse, parse_string, lexer())
    
    def test_semantic_action_2_with_success(self):
      parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())
      self.assertEqual(SemanticTools.main_identifier, "teste")
    
    def test_semantic_action_2_with_fail(self):
        self.assertParserError(u"def teste : \n [ teste := 0; input(teste);  ]", u"Erro na linha 2 - identificador teste já declarado anteriormente")
    
    def test_semantic_action_5(self):
      parser.parse(u"def teste : \n [ esse, outro := 0; input(esse);  ]", lexer())
      self.assertTrue(SemanticTools.symbol_table["esse"])    
      self.assertTrue(SemanticTools.symbol_table["outro"])

    def test_semantic_error_with_input(self):
      self.assertParserError(u"def teste : \n [ input(lado);  ]", u"Erro na linha 2 - identificador lado não declarado")

    def test_semantic_success_with_input(self):
      parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())
