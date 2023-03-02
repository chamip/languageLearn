#python -m unittest
import unittest
from sentence import Sentence

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("Hello World!")
        self.sentence1 = Sentence("aBc 123w")
    
    def test_letter_count(self):
        self.assertEqual(self.sentence.letter_count(), 12)
    
    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper_alpha_count(self):
        self.assertNotEqual(self.sentence.upper_alpha_count(), 3)
        self.assertEqual(self.sentence1.upper_alpha_count(), 1)