# -*- coding: utf-8 -*-

import unittest
from tokenizer import Tokenizer

class TokenizerTestCase(unittest.TestCase):
    """ Tests for tokenizer.py """

    def setup(self):
        # tokenizer = Tokenizer("test.prf", "test.rules")
        pass

    def test_characters(self):
        t = Tokenizer()
        result = t.characters("Màttís List")
        self.assertEqual(result, "M a ̀ t t i ́ s # L i s t")

        t = Tokenizer("test.prf", "test.rules")
        result = t.characters("Màttís List")
        self.assertEqual(result, "M a ̀ t t i ́ s # L i s t")

    def test_graphemes(self):
        t = Tokenizer()
        result = t.graphemes("Màttís List")
        self.assertEqual(result, "M à t t í s # L i s t")

        t = Tokenizer("test.prf", "test.rules")
        result = t.graphemes("Màttís List")
        self.assertEqual(result, "M à tt í s # ? ? s ?")

    def test_grapheme_clusters(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.grapheme_clusters("Màttís List")
        self.assertEqual(result, "M à t t í s # L i s t")
        
    def test_transform(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.transform("Màttís List")
        self.assertEqual(result, "M à tt í s # ? ? s ?")

    def test_transform(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.transform("Màttís List", 'ipa')
        self.assertEqual(result, "m a tː i s # ? ? s ?")

    def test_transform(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.transform("Màttís List", 'funny')
        self.assertEqual(result, "J e l n a # ? ? a ?")

    def test_rules(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.rules("Màttís List")
        self.assertEqual(result, "Jelena")

    def test_transform_rules(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.transform_rules("Màttís List")
        self.assertEqual(result, "M à e l ?")

	def test_find_missing_characters(self):
        t = Tokenizer("test.prf", "test.rules")
        result = t.find_missing_characters("L i s t")
        self.assertEqual(result, "? ? s ?")

if __name__=="__main__":
    unittest.main()
