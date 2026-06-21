class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # start l at the beginning
        r = 1 # start r right after l
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1 # r needs to move forward after this check
            else:
                l = r
                r += 1

        return maxProfit

        