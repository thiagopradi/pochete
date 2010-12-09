# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser, SemanticTools

class TestSintatic(MockerTestCase):  
    def setUp(self):
      self.var_lex = lexer()
      SemanticTools.reset()
      
    def assertParserError(self, parse_string, error):
        self.assertRaisesRegexp(Exception, error, parser.parse, parse_string, lexer())
        
    def test_sintatic_exception_with_line_number(self):
        self.assertParserError(u"def teste : := 1; \n b := 2;  ]", u'Erro na linha 1 - encontrado :=, esperado construção sintática válida')

    def test_sintatic_exception(self):
        self.assertParserError(u"def teste ab [ c := 1; \n d := 2;  ]", u'Erro na linha 1 - encontrado ab, esperado construção sintática válida')
      
    def test_with_only_def(self):
        self.assertParserError(u"def", "Erro na linha 1 - encontrado EOF, esperado identificador")
    
    def test_with_def_and_identifier(self):
        self.assertParserError(u"def abc", "Erro na linha 1 - encontrado EOF, esperado ':'")
      
    def test_with_def_and_identifier_and_symbol(self):
        self.assertParserError(u"def abc : ", "Erro na linha 1 - encontrado EOF, esperado '\['")

    def test_with_def_and_identifier_and_other_symbol(self):
        self.assertParserError(u"def abc : [ ", "Erro na linha 1 - encontrado EOF, esperado comando")

    def test_with_def_and_identifier_and_symbol_other(self):
       self.assertParserError(u"def abc : [ a := a+1;", "Erro na linha 1 - encontrado EOF, esperado '\]'")
