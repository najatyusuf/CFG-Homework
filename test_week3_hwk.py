from unittest import TestCase
from week3_hwk import generate_phrase

class TestGeneratePhrase(TestCase):

    def testEmptyString(self):
        self.assertTrue(generate_phrase("", ""))

    def testBlankSpaces(self):
        self.assertTrue(generate_phrase(" ", " "))

    def testEmptyPhrase(self):
        self.assertTrue(generate_phrase("A", ""))

    def testEqualStrings(self):
        self.assertTrue(generate_phrase("aBc?", "aBc?"))

    def testLowerStrings(self):
        self.assertTrue(generate_phrase("abc", "abc"))

    def testUpperStrings(self):
        self.assertTrue(generate_phrase("ABC", "ABC"))

    def testMoreCharactersInString(self):
        self.assertTrue(generate_phrase("aabbcc", "abc"))

    def testMoreCharacterInPhrases(self):
        self.assertFalse(generate_phrase("abc", "aabbcc"))

    def testLowerPhrase(self):
        self.assertFalse(generate_phrase("ABC", "abc"))

    def testUpperPhrase(self):
        self.assertFalse(generate_phrase("abc", "ABC"))