import unittest
import beeflower

class Testbeeflower(unittest.TestCase):
	def setUp(self):
		print("Set up goes here")

	def test_hello_word(self):
		self.assertEqual("Hello world", "Hello world")


