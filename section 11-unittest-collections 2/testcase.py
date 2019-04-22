# Run this program as python testcase.py -v

import unittest # Importing Python's standard unittest
from myfunc import multby2, isEven

# We need a class that inherits from unittest.TestCase
class AllTests(unittest.TestCase):

	# The method name has to start with test_
	# So one can have more methods that do not start 
	# with test_ as support functions
	
	def test_multby2test(self):
		self.assertEqual(multby2(4), 8)
		
	def test_checkeven(self):
		self.assertTrue(isEven(4))
		self.assertFalse(isEven(5))
	
# Call unittest.main()
if __name__ == "__main__":	
	unittest.main()
