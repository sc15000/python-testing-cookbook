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

class RomanNumeralConverterTest(unittest.TestCase)
	"""
	The TestCase class, inherited from unittest.TestCase within 
	the unittest module; Python's defacto test framework module.

	It's convention for readibility to model the name of the class 
	on that of the DUT class, appended with "Test".
	"""

	def test_parsing_millenia(self):
		"""
		Verify that the DUT correctly parses Millenia

		It is necessary to prepend all tests with "test",
		making it visible to unittest and allowing it to pick 
		up the test automatically
		"""
		value = RomanNumeralConverter("M")
		self.assertEquals(value.convert_to_decimal(), 1000)

	# Various other test go here for comprehensive testing...

	def test_parsing_one(self):
		"""
		Verify that the DUT correctly parses units
		"""
		value = RomanNumeralConverter("I")
		self.assertEquals(value.convert_to_decimal(), 1)

	# It's as important to verify correct handling of invalid inputs
	# as for valid inputs.

	def test_empty_roman_numeral(self):
		"""
		Verify that the DUT gracefully rejects empty strings
		"""
		value = RomanNumeralConverter("")
		self.assertTrue(value.convert_to_decimal() == 0)
		self.assertFalse(value.convert_to_decimal() > 0)
	
	def test_no_roman_numeral(self):
		"""
		Verify that the DUT gracefully rejects empty object
		"""
		value = RomanNumeralConverter(None)
		self.assertRaises(TypeError, value.convert_to_decimal)


# Finally, allow the above test cases to be run if this script is executed 
# (as opposed to being imported)

if __name__ == "__main__":
	unittest.main()
		

