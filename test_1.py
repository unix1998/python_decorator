import unittest

class simple_test(unittest.TestCase):
	def setUp(self):
    	 self.foo = list(range(10))

	def test_1st(self):
    	 self.assertEqual(self.foo.pop(),9)

	def test_2nd(self):
    	 self.assertEqual(self.foo.pop(),9)

if __name__ == '__main__':
	unittest.main()
