import unittest
import mylib

class TestAnagram(unittest.TestCase):
    def test_add(self):
		#This test should pass.
        self.assertTrue(mylib.is_anagram("cinema", "iceman"))
		
		#This one will fail.   Comment it in to see the test fail.
		#self.assertTrue(mylib.is_anagram("leora", "iceman"))
