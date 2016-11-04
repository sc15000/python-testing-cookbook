class RomanNumeralConverter(object):
    """
    The DUT class - A simple Roman Numeral Converter
    """
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        self.numeral_map = ((1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I"))
    def convert_to_decimal(self, numeral):
        val = 0
        for char in numeral:
            val += self.digit_map[char]
        if val > 2000:
            raise ValueError("Values greater than 2000 are unsupported.")
        return val

    def convert_to_numeral(self, digit):
        if digit > 2000:
            raise ValueError("Values greater than 2000 are unsupported.")

        # Reset to millenia, the largest quanta of Roman numeral  
        numeral_string = ""      
        
        # Go through each of the Roman Numerals, accounting for each as appropriate
        for (value, numeral) in self.numeral_map:
            while digit >= value:
                numeral_string += numeral
                digit -= value
        return numeral_string
        
import unittest

class RomanNumeralConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = RomanNumeralConverter()
        self.rn_to_d = self.converter.convert_to_decimal
        self.d_to_rn = self.converter.convert_to_numeral

    def test_valid_input(self):
        """Verify that 'ordinary' valid input is correctly processed
        """
        # All we do here is define the test parameters
        tests = (
                    (self.rn_to_d, "equals", "CLXVIII", 168),
                    (self.rn_to_d, "equals", "CLXVI", 166),
                    (self.rn_to_d, "equals", "CLXVIIII", 169),
                    (self.rn_to_d, "equals", "CLVIII", 158),
                    (self.d_to_rn, "equals", 25, "XXV"),
                    (self.d_to_rn, "equals", 225, "CCXXV"),
                    (self.d_to_rn, "equals", 19, "XIVIII"), # Deliberately failing test
                    (self.d_to_rn, "equals", 987, "DCCCCLXXXVII"),
                    (self.d_to_rn, "equals", 450, "CCCCL")
                )    
        # List comprehension is just a more succinct form of 'for' loop
        [self.verify(test) for test in tests]

    def test_corner_cases(self):
        """Verify that the DUT behaves correctly either side of the valid/invalid 
        value boundary
        """
        tests = (
                    (self.rn_to_d, "equals", "MM", 2000),
                    (self.rn_to_d, "raises", "MMI", ValueError),
                    (self.d_to_rn, "equals", 2000, "MM"),
                    (self.d_to_rn, "raises", 2001, ValueError)
                )
        [self.verify(test) for test in tests]
    
    def test_invalid_types(self):
        """Verify that empty or invalid input types are handled gracefully"""
        tests = (
                    (self.rn_to_d, "equals", "", 0),
                    (self.rn_to_d, "raises", None, TypeError),
                    (self.d_to_rn, "equals", 0, ""),
                    (self.d_to_rn, "equals", None, "")
                )
        [self.verify(test) for test in tests]


    def verify(self, test_params):
        """The workhorse of the TestCase test class - a generic approach to covering 
        all types of tests for this DUT class.
        """
        # Split for readability
        (test_method, test_condition, test_input, expected_test_output) = test_params
        
        # Provide test progress feedback
        print "\nTesting that '%s' (input) %s '%s' (output)..." % (test_input, test_condition, expected_test_output)

        # Test behaviour depends on condition:        
        if test_condition == "equals":
            self.assertEquals(test_method(test_input), expected_test_output)
        elif test_condition == "raises":
            self.assertRaises(expected_test_output, test_method, test_input)
        else:
            raise ValueError("Unknown test condition: '%s'!" % test_condition)
        
        print "PASS"


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
