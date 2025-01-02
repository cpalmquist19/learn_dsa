from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers we've seen and their indices
        # Key = number we've seen, Value = index where we saw it
        prevMap = {}

        for i, n in enumerate(nums):
            # Calculate what number we need to find (the complement)
            diff = target - n

            # If we've seen the number we need, we found our pair!
            if diff in prevMap:
                return [prevMap[diff], i]  # Return [index of diff, current index]

            # Haven't found pair yet, remember current number and its index
            prevMap[n] = i

        return