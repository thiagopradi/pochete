import unittest
from lexer import lexer
from pochete_parser import parser

class TestSequenceFunctions(unittest.TestCase):  
    def setUp(self):
      self.var_lex = lexer()
      
    def test_tokens(self):
      self.var_lex.input("a := 1")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "a")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, ":=")
      tok = self.var_lex.token()    
      self.assertEqual(tok.value, "1")

if __name__ == '__main__':
    unittest.main()