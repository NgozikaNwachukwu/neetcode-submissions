class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the algorithm is to buy when its low and sell when high
        #so we have two pointers, one af the beginning and one in front of that one
        # the r pointer is for selling(so ideally it should land on a number larger than prices[l])
        # the l pointer should only move to r's position if prices[l] is greater than prices[r]
        #because think about it, l should be on the lowest value, so we can know that since we bought 
        # this stock thats low, to get the max profit, we need to check the higher prices
        #so r should always be higher than l, so we can keep selling to check the max profit
        # and if r is less, we move it forward(but move l first cuz l needs to get to that lower position)
        l = 0 #starts at the beginning
        r = 1 # starts right after l
        maxProfit = 0 # initiailizing to 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1
            else:
                l = r
                r += 1
        return maxProfit