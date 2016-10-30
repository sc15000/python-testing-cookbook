class RomanNumeralConverter(object):
	"""
	The DUT class - A simple Roman Numeral Converter
	"""
	def __init__(self):
		self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

	def convert_to_decimal(self, roman_numeral):
		val = 0
		for char in roman_numeral:
			val += self.digit_map[char]
		return val

	
import unittest

class RomanNumeralConverterTest(unittest.TestCase):
	"""
	"""
	def setUp(self):
		"""
		Prepare for test
		"""
		print "Preparing for test by creating a RomanNumeralConverter"
		self.cvt = RomanNumeralConverter()


	def tearDown(self):
		"""
		Clean up after test
		"""
		print "Cleaning up test by deleting a RomanNumeralConverter"
		self.cvt = None
		
	def test_parsing_millenia(self):
		"""
		Verify that the DUT correctly parses Millenia
		"""
		self.assertEquals(self.cvt.convert_to_decimal("M"), 1000)

	def test_parsing_one(self):
		"""
		Verify that the DUT correctly parses units
		"""
		self.assertEquals(self.cvt.convert_to_decimal("I"), 1)

	def test_empty_roman_numeral(self):
		"""
		Verify that the DUT gracefully rejects empty strings
		"""
		self.assertTrue(self.cvt.convert_to_decimal("") == 0)
		self.assertFalse(self.cvt.convert_to_decimal("") > 0)
	
	def test_no_roman_numeral(self):
		"""
		Verify that the DUT gracefully rejects empty object
		"""
		self.assertRaises(TypeError, self.cvt.convert_to_decimal)

if __name__ == "__main__":
	unittest.main()
		

