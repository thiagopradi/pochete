# coding: utf-8
import unittest
from mocker import MockerTestCase
from lexer import lexer
from pochete_parser import parser
from pochete_parser import SemanticTools

class TestCodeGeneration(MockerTestCase):
  def setUp(self):
    SemanticTools.reset()
  
  def assertParserError(self, parse_string, error):
      self.assertRaisesRegexp(Exception, error, parser.parse, parse_string, lexer())
  
  # This test is for generating header, footer, and allocating integer variables
  def test_code_generation_header_footer_and_allocating_integer(self):
    parser.parse(u"def teste : \n [ a := 1; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 1       stloc a\n        ret\n        }\n        }\n      ')

  # This test is for generating header, footer, and allocating integer variables, to not duplicate vars
  def test_code_generation_header_footer_and_allocating_integer_duplicated(self):
    parser.parse(u"def teste : \n [ a := 1; a := 2;]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 1       stloc a        ldc.i4 2       stloc a\n        ret\n        }\n        }\n      ')
  
  def test_allocating_real(self):
    parser.parse(u"def teste : \n [ a := 1.0; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (float32 a)        ldc.r4  1.0\n        ret\n        }\n        }\n      ')

  def test_allocating_bool_true(self):
    parser.parse(u"def teste : \n [ a := true; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4  1        stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_bool_false(self):
    parser.parse(u"def teste : \n [ a := false; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4  0        stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_binary(self):
    parser.parse(u"def teste : \n [ a := 0b0101; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 5       stloc a\n        ret\n        }\n        }\n      ')
  
  def test_allocating_hexadecimal(self):
    parser.parse(u"def teste : \n [ a := 0x01AF; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 431       stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_octal(self):
    parser.parse(u"def teste : \n [ a := 0o0132; ]", lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 90       stloc a\n        ret\n        }\n        }\n      ')

  def test_allocating_literal(self):
    parser.parse(u'def teste : \n [ a := "foo"; ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (string a)        ldstr "foo"        stloc a\n        ret\n        }\n        }\n      ')

  def test_input_with_error(self):
    self.assertParserError(u'def teste : \n [input(abc); ]', u'Erro na linha 2 - identificador abc n\xe3o declarado' )
  
  def test_input_with_integer(self):
    parser.parse(u'def teste : \n [ a := 0; input(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 0       stloc acall string [mscorlib]System.Console::ReadLine()call int32 [mscorlib]System.Int32::Parse(string)stloc a\n        ret\n        }\n        }\n      ')

  def test_input_with_binary(self):
    parser.parse(u'def teste : \n [ a := 0b010; input(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 2       stloc acall string [mscorlib]System.Console::ReadLine()call int32 [mscorlib]System.Int32::Parse(string)stloc a\n        ret\n        }\n        }\n      ')

  def test_input_with_octal(self):
    parser.parse(u'def teste : \n [ a := 0o032; input(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 26       stloc acall string [mscorlib]System.Console::ReadLine()call int32 [mscorlib]System.Int32::Parse(string)stloc a\n        ret\n        }\n        }\n      ')

  def test_input_with_hexadecimal(self):
    parser.parse(u'def teste : \n [ a := 0x012; input(a); ]', lexer())    
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 18       stloc acall string [mscorlib]System.Console::ReadLine()call int32 [mscorlib]System.Int32::Parse(string)stloc a\n        ret\n        }\n        }\n      ')

  def test_input_with_real(self):
    parser.parse(u'def teste : \n [ a := 1.0; input(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (float32 a)        ldc.r4  1.0call string [mscorlib]System.Console::ReadLine()call float32 [mscorlib]System.Float32::Parse(string)stloc a\n        ret\n        }\n        }\n      ')

  def test_input_string(self):
    parser.parse(u'def teste : \n [ a := "foo"; input(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (string a)        ldstr "foo"        stloc acall string [mscorlib]System.Console::ReadLine()stloc a\n        ret\n        }\n        }\n      ')
  
  def test_output_with_integer(self):
    parser.parse(u'def teste : \n [ a := 0; input(a); output(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 a)        ldc.i4 0       stloc acall string [mscorlib]System.Console::ReadLine()call int32 [mscorlib]System.Int32::Parse(string)stloc a        ldloc a        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')

  def test_output_with_real(self):
    parser.parse(u'def teste : \n [ a := 1.0; input(a); output(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (float32 a)        ldc.r4  1.0call string [mscorlib]System.Console::ReadLine()call float32 [mscorlib]System.Float32::Parse(string)stloc a        ldloc a        call void [mscorlib]System.Console::Write(float32)\n        ret\n        }\n        }\n      ')
  
  def test_output_with_string(self):
    parser.parse(u'def teste : \n [ a := "abc"; input(a); output(a); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (string a)        ldstr "abc"        stloc acall string [mscorlib]System.Console::ReadLine()stloc a        ldloc a        call void [mscorlib]System.Console::Write(string)\n        ret\n        }\n        }\n      ')
    
  def test_output_with_error(self):
    self.assertParserError(u'def teste : \n [ output(abc); ]', u'Erro na linha 2 - identificador abc n\xe3o declarado' )

  def test_sum(self):
    parser.parse(u'def teste : \n [ xpto := 1; b := 2; xpto := xpto + b; output(xpto); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n add\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')
  
  def test_sub(self):
    parser.parse(u'def teste : \n [ xpto := 1; b := 2; xpto := xpto - b; output(xpto); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n sub\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')

  def test_mul(self):
    parser.parse(u'def teste : \n [ xpto := 1; b := 2; xpto := xpto * b; output(xpto); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n mul\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')

  def test_div(self):
    parser.parse(u'def teste : \n [ xpto := 1; b := 2; xpto := xpto / b; output(xpto); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n div\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')
  
  def test_rem(self):
    parser.parse(u'def teste : \n [ xpto := 1; b := 2; xpto := xpto % b; output(xpto); ]', lexer())
    self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n rem\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')
  
  # def test_final(self):
  #   string = u"""def quadrado : [
  #   lado := 0;
  #   input (lado);
  #   area := lado * lado;
  #   output (area);
  #   ]"""
  #   parser.parse(string, lexer())
  #   self.assertEqual(''.join(SemanticTools.code), '.assembly extern mscorlib{}\n    .assembly teste{}\n    .module teste.exe\n    .class public teste\n    {\n    .method public static void principal ()\n    {\n    .entrypoint        .locals init (int32 xpto)        .locals init (int32 b)        ldc.i4 1       stloc xpto        ldc.i4 2       stloc b        ldloc xpto\n        ldloc b\n rem\n stloc xpto        ldloc xpto        call void [mscorlib]System.Console::Write(int32)\n        ret\n        }\n        }\n      ')

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
  
