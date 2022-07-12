import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello")["translations"][0]["translation"], "Bonjour")
        self.assertNotEqual(english_to_french("None")["translations"][0]["translation"], "")
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour")["translations"][0]["translation"], "Hello")
        self.assertNotEqual(french_to_english("None")["translations"][0]["translation"], "")

if __name__ == "__main__":
    unittest.main()
