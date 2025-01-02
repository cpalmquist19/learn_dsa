from typing import List

class Solution:

    def max_profit(self, prices: List[int]) -> int:

        buy, sell = 0, 1
        max_profit = 0

        # Don't look beyond the last price
        while sell < len(prices):

            # If we find a better price to buy at, update the buy index
            if prices[buy] < prices[sell]:

                # Calculate profit
                profit = prices[sell] - prices[buy]

                # Update max_profit if we found a better profit
                max_profit = max(max_profit, profit)

            else:

                # Move the buy index to the sell index
                buy = sell

            # Move the sell index to the next price
            sell += 1

        return max_profit