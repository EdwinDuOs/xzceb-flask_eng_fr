import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TranslatorTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        translation = englishToFrench("Hello")
        self.assertEqual(translation, "Bonjour")

    def test_english_to_french_apple(self):
        translation = englishToFrench("apple")
        self.assertEqual(translation, "pomme")

    def test_french_to_english_bonjour(self):
        translation = frenchToEnglish("Bonjour")
        self.assertEqual(translation, "Hello")

    def test_french_to_english_maison(self):
        translation = frenchToEnglish("maison")
        self.assertEqual(translation, "house")

    def test_english_to_french_hello_not_equal(self):
        translation = englishToFrench("Hello")
        self.assertNotEqual(translation, "Hi")

    def test_english_to_french_apple_not_equal(self):
        translation = englishToFrench("apple")
        self.assertNotEqual(translation, "pomme")

    def test_french_to_english_bonjour_not_equal(self):
        translation = frenchToEnglish("Bonjour")
        self.assertNotEqual(translation, "Salut")

    def test_french_to_english_maison_not_equal(self):
        translation = frenchToEnglish("maison")
        self.assertNotEqual(translation, "home")

if __name__ == "__main__":
    unittest.main()

