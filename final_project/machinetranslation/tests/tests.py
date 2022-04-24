import unittest
# from ../translator import english_to_french
# from ../translator import french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_e2f_1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_e2f_none(self):
        self.assertNotEqual(english_to_french("None"), '')

    def test_e2f_null(self):
        self.assertNotEqual(english_to_french(0), 0)


class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e_1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_f2e_none(self):
        self.assertNotEqual(french_to_english("None"), '')

    def test_f2e_null(self):
        self.assertNotEqual(french_to_english(0), 0)


unittest.main()
