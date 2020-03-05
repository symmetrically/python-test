# Write a function that, given a string, returns its longest palindromic substring. 
# A palindrome is defined as a string that is written the same forward and backward. 
# Assume that there will only be one longest palindromic substring.

# Sample input: "abaxyzzyxf"
# Sample output: "xyzzyx"

import unittest

def longestPalindromicSubstring(string):
    pass

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestPalindromicSubstring("a"),"a")
    
    def test_case_2(self):
        self.assertEqual(longestPalindromicSubstring("it's a highnoon"),"noon")

    def test_case_3(self):
        self.assertEqual(longestPalindromicSubstring("abccbait's highnoon"),"abccba")

    def test_case_4(self):
        self.assertEqual(longestPalindromicSubstring("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"),"zzzzzzzzzzzzzzzzzzzz")

    def test_case_5(self):
        self.assertEqual(longestPalindromicSubstring("zzzzzzz2345abbbba5432zzbbababa"),"zz2345abbbba5432zz")




if __name__ == "__main__":
    unittest.main()

    