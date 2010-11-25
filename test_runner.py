# coding: utf-8
import unittest

from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser

from test.test_sintatic import TestSintatic
from test.test_lexer import TestLexer
from test.test_semantic import TestSemantic
from test.test_code_generation import TestCodeGeneration

if __name__ == '__main__':
    unittest.main()