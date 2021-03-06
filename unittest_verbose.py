class RomanNumeralConverter(object):
    """
    The DUT class - A simple Roman Numeral Converter
    """
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    def convert_to_decimal(self):
        val = 0
        for char in self.roman_numeral:
            val += self.digit_map[char]
        return val

    
import unittest

class RomanNumeralConverterTest(unittest.TestCase):
    """
    The TestCase class, inherited from unittest.TestCase within 
    the unittest module; Python's defacto test framework module.

    It's convention for readibility to model the name of the class 
    on that of the DUT class, appended with "Test".
    """

    def test_parsing_millenia(self):
        """This test will fail, and this docstring will appear on the console during the test

        It is necessary to prepend all tests with "test",
        making it visible to unittest and allowing it to pick 
        up the test automatically
        """
        value = RomanNumeralConverter("M")
        self.assertEquals(value.convert_to_decimal(), 999)

    def test_parsing_one(self):
        """
        Verify that the DUT correctly parses units
        """
        value = RomanNumeralConverter("I")
        self.assertEquals(value.convert_to_decimal(), 1)

    def test_empty_roman_numeral(self):
        """
        Verify that the DUT gracefully rejects empty strings
        """
        value = RomanNumeralConverter("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    
    def test_no_roman_numeral(self):
        """This test will error, and this docstring will appear on the console during the test
        """
        value = RomanNumeralConverter(None)
        self.assertRaises(IndexError, value.convert_to_decimal)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
