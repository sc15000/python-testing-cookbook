class RomanNumeralConverter(object):
    """
    The DUT class - A simple Roman Numeral Converter
    """
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    def convert_to_decimal(self, numeral):
        val = 0
        for char in numeral:
            val += self.digit_map[char]
        return val


class RomanNumeralConverterTest(object):

    def __init__(self):
        self.converter = RomanNumeralConverter()

    def test_parsing_millenium(self):
        """Verify the DUT correctly parses millenia"""
        assert self.converter.convert_to_decimal("M") == 1000

    def test_parsing_century(self):
        """Verify the DUT correctly parses centuries"""
        assert self.converter.convert_to_decimal("C") == 100

    def test_parsing_one(self):
        """Verify the DUT correctly parses units"""
        assert self.converter.convert_to_decimal("I") == 1

    def test_empty_roman_numeral(self):
        """Verify the DUT correctly rejects empty strings"""
        assert self.converter.convert_to_decimal("") == 0 

import unittest

if __name__ == "__main__":

    tester = RomanNumeralConverterTest() 
    # Wrap each of the test methods in unittest's FunctionTestCase()
    unittest_tests = [
            tester.test_parsing_millenium,
            tester.test_parsing_century,
            tester.test_parsing_one,
            tester.test_empty_roman_numeral
            ]

    suite = unittest.TestSuite()
    for test in unittest_tests:
        testcase = unittest.FunctionTestCase(test)
        suite.addTest(testcase)
    
    unittest.TextTestRunner(verbosity=2).run(suite)
        
        
