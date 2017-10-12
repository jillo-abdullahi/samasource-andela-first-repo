import unittest
from divide_two_numbers import divide_two_numbers

class TestDivision(unittest.TestCase):

	def test_basic_division(self):
		self.assertEqual(divide_two_numbers(10,2), 5)
	def test_edge_case(self):
		self.assertEqual(divide_two_numbers(-15,-3), 5)
	def test_edge_case_two(self):
		self.assertEqual(divide_two_numbers(-500,2), -250)
	def test_float_answer(self):
		self.assertEqual(divide_two_numbers(5,2), 2.5)

if __name__ == '__main__':
	unittest.main()



