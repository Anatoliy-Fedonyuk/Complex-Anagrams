"""--Unit tests for module complex anagrams--"""
from unittest import TestCase, main
from anagrams.anagrams import get_anagram


class AnagramsTest(TestCase):
    def test_word(self):
        self.assertEqual(get_anagram("cad*kuf*cad"), "dac*fuk*dac")
        self.assertEqual(get_anagram("d"), "d")
        self.assertEqual(get_anagram("c!"), "c!")
        self.assertEqual(get_anagram("c!2784!d"), "d!2784!c")

    def test_words(self):
        self.assertEqual(get_anagram("only you"), 'ylno uoy')
        self.assertEqual(get_anagram("a1bcd efg!h"), "d1cba hgf!e")
        self.assertEqual(get_anagram("Anatol12 !read$$$$$ 0 das bot33.33"), "lotanA12 !daer$$$$$ 0 sad tob33.33")
        self.assertEqual(get_anagram("c!!!ad kuf ca34d"), "d!!!ac fuk da34c")
        self.assertEqual(get_anagram("12345 !@#$"), "12345 !@#$")

    def test_empty_string(self):
        with self.assertRaises(ValueError) as e:
            get_anagram("")
        self.assertEqual('--Anagram do not make sense, string empty--', e.exception.args[0])

    def test_type_number(self):
        with self.assertRaises(TypeError) as e:
            get_anagram(1234500)
        self.assertEqual('--Only a string can be used as input!--', e.exception.args[0])

    def test_type_dict(self):
        with self.assertRaises(TypeError) as e:
            get_anagram({'a': 11, 'b': 22, 'c': 33})
        self.assertEqual("unhashable type: 'dict'", e.exception.args[0])

    def test_type_list(self):
        with self.assertRaises(TypeError) as e:
            get_anagram([1, -22, 3, 4, -65])
        self.assertEqual("unhashable type: 'list'", e.exception.args[0])

    def test_type_tuple(self):
        with self.assertRaises(TypeError) as e:
            get_anagram(('avcb', 'eefdf'))
        self.assertEqual('--Only a string can be used as input!--', e.exception.args[0])

    def test_type_none(self):
        with self.assertRaises(TypeError) as e:
            get_anagram(None)
        self.assertEqual('--Only a string can be used as input!--', e.exception.args[0])

    def test_string_of_digit(self):
        with self.assertRaises(ValueError) as e:
            get_anagram("12345 67890")
        self.assertEqual('--Anagram do not make sense in your string only digits--', e.exception.args[0])


if __name__ == '__main__':
    main()
