import unittest
from sliding_window import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        # Test case 1: Simple increasing prices
        self.assertEqual(self.solution.max_profit([1, 2, 3, 4, 5]), 4)

        # Test case 2: Simple decreasing prices (no profit possible)
        self.assertEqual(self.solution.max_profit([5, 4, 3, 2, 1]), 0)

        # Test case 3: Example from common stock problem
        self.assertEqual(self.solution.max_profit([7, 1, 5, 3, 6, 4]), 5)

        # Test case 4: Empty list
        self.assertEqual(self.solution.max_profit([]), 0)

        # Test case 5: Single price (no profit possible)
        self.assertEqual(self.solution.max_profit([1]), 0)

        # Test case 6: Two prices with profit
        self.assertEqual(self.solution.max_profit([3, 8]), 5)

        # Test case 7: Two prices with no profit
        self.assertEqual(self.solution.max_profit([8, 3]), 0)

        # Test case 8: Multiple peaks and valleys
        self.assertEqual(self.solution.max_profit([3, 2, 6, 5, 0, 3]), 4)

    def test_edge_cases(self):
        # Test with negative numbers (not typically valid for stock prices but good to test)
        self.assertEqual(self.solution.max_profit([-1, -5, -3, -2]), 3)

        # Test with repeated numbers
        self.assertEqual(self.solution.max_profit([2, 2, 2, 2]), 0)

        # Test with large numbers
        self.assertEqual(self.solution.max_profit([1000, 2000, 500, 5000]), 4500)

if __name__ == '__main__':
    unittest.main()