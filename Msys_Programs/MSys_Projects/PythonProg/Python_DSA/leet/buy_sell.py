# def maxProfit(prices):
#         total_days = len(prices)
#         min_prices = prices[0]
#         profit = 0
#         for i in range(1, total_days):
#             diff= prices[i] - min_prices
#             if diff > profit:
#                 profit = diff
#             elif prices[i]<min_prices:
#                 min_prices = prices[i]
#         return profit


class Solution:
    def maxProfit(self, prices):
        total_days = len(prices)
        min_prices = prices[0]
        profit = 0
        for i in range(1, total_days):
            diff= prices[i] - min_prices
            if diff > profit:
                profit = diff
            elif prices[i]<min_prices:
                min_prices = prices[i]
        return profit

# A = [9,6,2,4,5,3]
A = [5,6,2,4,5,3]
B =  Solution()
B.maxProfit(A)

# B = maxProfit(A)
print(A)
print(B)
print(B.maxProfit(A))
