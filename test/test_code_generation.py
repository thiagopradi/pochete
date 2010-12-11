# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser
from pochete_parser import SemanticTools

class TestCodeGeneration(unittest.TestCase):
  def setUp(self):
    SemanticTools.reset()
    
  # This test is for generating header, footer, and allocating integer variables
  def test_code_generation_header_footer_and_allocating_integer(self):
    parser.parse(u"def teste : \n [ a := 1; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4 1       stloc a\n        ret\n        }\n        }\n      ')

  # This test is for generating header, footer, and allocating integer variables, to not duplicate vars
  def test_code_generation_header_footer_and_allocating_integer_duplicated(self):
    parser.parse(u"def teste : \n [ a := 1; a := 2;]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4 1       stloc a        ldc.i4 2       stloc a\n        ret\n        }\n        }\n      ')
  
  def test_allocating_real(self):
    parser.parse(u"def teste : \n [ a := 1.0; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (float32 a)        ldc.r4  1.0\n        ret\n        }\n        }\n      ' )

  def test_allocating_bool_true(self):
    parser.parse(u"def teste : \n [ a := true; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4  1        stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_bool_false(self):
    parser.parse(u"def teste : \n [ a := false; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4  0        stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_binary(self):
    parser.parse(u"def teste : \n [ a := 0b0101; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4 5       stloc a\n        ret\n        }\n        }\n      ')
  
  def test_allocating_hexadecimal(self):
    parser.parse(u"def teste : \n [ a := 0x01AF; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4 431       stloc a\n        ret\n        }\n        }\n      ' )

  def test_allocating_octal(self):
    parser.parse(u"def teste : \n [ a := 0o0132; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (int32 a)        ldc.i4 90       stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_literal(self):
    parser.parse(u'def teste : \n [ a := "foo"; ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals (string a)        ldstr "foo"        stloc a\n        ret\n        }\n        }\n      ')  
  
  # def test_p_action16(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b + 1; if a or b : [ a := a+b; ]; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add        .locals (int32 a)        or\n add        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  #   
  # def test_p_action17(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b + 1; if a and b : [ a := a+b; ]; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add        .locals (int32 a)        and\n add        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  # 
  # def test_p_action23(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b + 1; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n add        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  #   
  # def test_p_action24(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b - 1; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n sub        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  # 
  # def test_p_action25(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b * 1; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n mul        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  # 
  # def test_p_action26(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b / 1; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n div        .locals (int32 a)\n      ret\n      }\n      }\n    ')
  # 
  # def test_p_action27(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := b % 1; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n rem\n      ret\n      }\n      }\n    ')
  # 
  # def test_p_action36(self):
  #   parser.parse(u"def teste : \n [ a := 0;  a := -a; ]", lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint\n        neg\n      ret\n      }\n      }\n    ')

  def test_p_action29(self):
    pass

  def test_p_action30(self):
    pass

  def test_p_action31(self):
    pass

  def test_p_action32(self):
    pass

  def test_p_action33(self):
    pass

  def test_p_action34(self):
    pass
  
  def test_p_action35(self):
    pass
  
