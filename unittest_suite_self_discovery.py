###
### DUT
###

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

###
### Test Cases
###

    
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


###
### Test Suite definitions
###

def suite_all():
    """All Test Cases in this module
    """
    suite1 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterBasicTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterEdgeCasesTest)
    return unittest.TestSuite([suite1, suite2])  

def suite_basic_excluding_one():
    """All Test Cases in the Basic set, except the 'ones' test
    """
    return unittest.TestSuite(
            map(RomanNumeralConverterBasicTest, ["test_parsing_millenium", "test_parsing_century"]))

def suite_empty_and_one():
    """Selecting just the invalid, empty-string test and the valid, ones test
    """
    suite = unittest.TestSuite()
    suite.addTest(RomanNumeralConverterEdgeCasesTest("test_empty_roman_numeral"))
    suite.addTest(RomanNumeralConverterBasicTest("test_parsing_one"))
    return suite

import argparse # For easy parsing of command-line arguments
import sys # For accessing command-line arguments

def usage():
    """Dynamically discover all tests suites and present them to the user for selection"""
    print "No test suites were specified for running!"

    this_module = sys.modules[__name__]
    module_item_names = dir(this_module)

    suites = [getattr(this_module, suite) for suite in module_item_names if suite.startswith('suite') and callable(getattr(this_module, suite))]

    for suite in suites:
        print suite.__name__, " : ", suite.__doc__

###
### Main()
###

if __name__ == "__main__":
    
    # If no test suite was specified at the command-line, the user needs some guidance:
    if len(sys.argv) != 2: # If just the script name was entered
        usage()
        sys.exit()
    else:
        try:
            suite = getattr(sys.modules[__name__], sys.argv[1])()
            unittest.TextTestRunner(verbosity=2).run(suite)
        except AttributeError:
            print "Unrecognised suite name '%s'" % sys.argv[1] 

