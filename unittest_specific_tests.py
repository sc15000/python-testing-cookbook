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
    The TestCase class
    """

    def test_parsing_millenia(self):
        """Verify the DUT correctly parses millenia"""
        value = RomanNumeralConverter("M")
        self.assertEquals(value.convert_to_decimal(), 1000)

    def test_parsing_one(self):
        """Verify the DUT correctly parses units"""
        value = RomanNumeralConverter("I")
        self.assertEquals(value.convert_to_decimal(), 1)

    def test_empty_roman_numeral(self):
        """Verify the DUT correctly rejects empty strings"""
        value = RomanNumeralConverter("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    
    def test_no_roman_numeral(self):
        """Verify the DUT correctly insists on being passed an object"""
        value = RomanNumeralConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)


if __name__ == "__main__":
    # 1 >unittest_specific_tests.py test_no_roman_numeral 
    
    # 2 According to whether or not tests were named on the command-line
    #   either add each test to the suite or add all tests from the test case class,
    #   respectively
    import sys
    if len(sys.argv) > 1:
        suite = unittest.TestSuite()
        for test in sys.argv[1:]:
            suite.addTest(RomanNumeralConverterTest(test))
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    
    # 3 Run the TextTestRunner as before
    unittest.TextTestRunner(verbosity=2).run(suite)
