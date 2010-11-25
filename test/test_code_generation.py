# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser
from pochete_parser import SemanticTools


class TestCodeGeneration(unittest.TestCase):
  def setUp(self):
    pass
    
  def test_should_create_the_header(self):
    pass
    #parser.parse(u"def teste : \n [ lado := 0; input(lado);  ]", lexer())
    #self.assertNotNil(SemanticTools.g_llvm_module)
