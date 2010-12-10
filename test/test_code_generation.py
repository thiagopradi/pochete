# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser
from pochete_parser import SemanticTools


class TestCodeGeneration(unittest.TestCase):
  def setUp(self):
    SemanticTools.reset()
  
  def test_p_action1_and_p_action2(self):
    parser.parse(u"def teste : \n [ a := 0; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n      ret\n      }\n      }\n    ')
  
  def test_p_action16(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b + 1; if a or b : [ a := a+b; ]; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add        or\n add\n      ret\n      }\n      }\n    ')
    
  def test_p_action17(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b + 1; if a and b : [ a := a+b; ]; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add        and\n add\n      ret\n      }\n      }\n    ')

  def test_p_action23(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b + 1; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add\n      ret\n      }\n      }\n    ' )
    
  def test_p_action24(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b - 1; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n sub\n      ret\n      }\n      }\n    ')
  
  def test_p_action25(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b * 1; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n mul\n      ret\n      }\n      }\n    ')
  
  def test_p_action26(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b / 1; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n div\n      ret\n      }\n      }\n    ')
  
  def test_p_action27(self):
    parser.parse(u"def teste : \n [ a := 0;  a := b % 1; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n rem\n      ret\n      }\n      }\n    ')
  
  def test_p_action36(self):
    parser.parse(u"def teste : \n [ a := 0;  a := -a; ]", lexer())
    self.assertEqual(SemanticTools.code, '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n        neg\n      ret\n      }\n      }\n    ')

  
  
