#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices is stock price with index as that i day's price
        minim, maxim = prices[0], prices[0]
        profit = 0
        for i in prices:
            if i > maxim:
                maxim = i
            if i< minim:
                minim = i
                maxim = 0 # setting maxim back to 0 as it's "behind" the new minimum so we can't access it anymore
            if profit < (maxim - minim):
                profit = maxim - minim
        return profit
# new approach - I realized after that there's no need to keep track on maximum rather just i - minim is what I needed 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices is stock price with index as that i day's price
        minim, maxim = prices[0], prices[0]
        profit = 0
        for i in prices:
            if i< minim:
                minim = i
            if profit < i - minim:
                profit = i - minim
        return profit
