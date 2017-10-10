import unittest
import divide_two_numbers

class TestDivision(unittest.TestCase):

	def test_divide_two_numbers(self):
		self.assertEqual(divide_two_numbers.divide_two_numbers(10,2), 5)
		self.assertEqual(divide_two_numbers.divide_two_numbers(-15,-3), 5)
		self.assertEqual(divide_two_numbers.divide_two_numbers(100,2), 50)
		self.assertEqual(divide_two_numbers.divide_two_numbers(5,2), 2.5)
		self.assertEqual(divide_two_numbers.divide_two_numbers(-500,2), -250)

if __name__ == '__main__':
	unittest.main()



