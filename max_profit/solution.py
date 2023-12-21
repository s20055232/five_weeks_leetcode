class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        idx = 0
        for buy in prices[idx:]:
            for sell in prices[idx + 1 :]:
                if sell - buy > profit:
                    profit = sell - buy

            idx += 1
        return profit

    def maxProfit2(self, prices: list[int]) -> int:
        profit = 0
        buy_place = 0
        for idx, p in enumerate(prices):
            diff = p - prices[buy_place]
            if diff < 0:
                buy_place = idx
            elif diff > profit:
                profit = diff
        return profit
