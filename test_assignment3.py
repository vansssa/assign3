import unittest
from assignment3 import sorted_str_and_sum

class TestAssignment1(unittest.TestCase):
	def test_sorted_str_and_sum(self) :
		self.assertEqual(sorted_str_and_sum('a2.txt') , 150)



if __name__ == '__main__':
    unittest.main()

