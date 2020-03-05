# Write a function that takes in two non-empty arrays of integers. 
# The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest 
# to zero. The function should return an array containing these two numbers, with the number from the first array in the first position. 
# Assume that there will only be one pair of numbers with the smallest difference.

# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
# Sample output: [28, 26]


import unittest

def smallestDifference(arrayOne, arrayTwo):
   pass


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 3],[26, 134, 135, 15, 17]),[20,17])

    def test_case_2(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]),[28, 26])

    def test_case_3(self):
        self.assertEqual(smallestDifference([10, 0, 20, 25],[1005, 1006, 1014, 1032, 1031]),[25,1005])

    def test_case_4(self):
        self.assertEqual(smallestDifference([10, 0, 20, 25, 2000],[1005, 1006, 1014, 1032, 1031]),[2000,1032])

    def test_case_5(self):
        self.assertEqual(smallestDifference([0, 20],[21, -2]),[20, 21])

        
        


if __name__ == "__main__":
    unittest.main()