from two_sum import Solution
import unittest

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.two_sum(nums, target), [0, 1])

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(self.solution.two_sum(nums, target), [2, 4])

    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.two_sum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()