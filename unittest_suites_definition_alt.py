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

class RomanNumeralConverterBasicTest(unittest.TestCase):
    """The Test Case for the basic, valid input tests"""

    def test_parsing_millenium(self):
        """Verify the DUT correctly parses millenia"""
        value = RomanNumeralConverter("M")
        self.assertEquals(value.convert_to_decimal(), 1000)

    def test_parsing_century(self):
        """Verify the DUT correctly parses centuries"""
        value = RomanNumeralConverter("C")
        self.assertEquals(value.convert_to_decimal(), 100)

    def test_parsing_one(self):
        """Verify the DUT correctly parses units"""
        value = RomanNumeralConverter("I")
        self.assertEquals(value.convert_to_decimal(), 1)

class RomanNumeralConverterEdgeCasesTest(unittest.TestCase):
    """The Test Case for the invalid input (i.e. corner/edge) tests"""

    def test_empty_roman_numeral(self):
        """Verify the DUT correctly rejects empty strings"""
        value = RomanNumeralConverter("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    
    def test_no_roman_numeral(self):
        """Verify the DUT correctly insists on being passed an object"""
        value = RomanNumeralConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)

def all():
    """All Test Cases in this module

        Compiling a suite list
    """
    suite1 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterBasicTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterEdgeCasesTest)
    return unittest.TestSuite([suite1, suite2])  

def basic_excluding_one():
    """All Test Cases in the Basic set, except the 'ones' test
       
        Using 'map' to pass each chosen test method by string to its Test Case class 
        constructor, which returns a TestCase object
    """
    return unittest.TestSuite(
            map(RomanNumeralConverterBasicTest, ["test_parsing_millenium", "test_parsing_century"]))

def empty_and_one():
    """Selecting just the invalid, empty-string test and the valid, ones test
     
        Individual test case addition
    """
    suite = unittest.TestSuite()
    suite.addTest(RomanNumeralConverterEdgeCasesTest("test_empty_roman_numeral"))
    suite.addTest(RomanNumeralConverterBasicTest("test_parsing_one"))
    return suite

if __name__ == "__main__":
    for suite_func in [all, basic_excluding_one, empty_and_one]:
        print "Running suite '%s'" % suite_func.__name__
        suite = suite_func()
        unittest.TextTestRunner(verbosity=2).run(suite)

        
