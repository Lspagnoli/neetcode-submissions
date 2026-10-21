class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l+1

        maxProfit = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                sale = prices[r] - prices[l]
                maxProfit = max(maxProfit, sale)
            else:
                l = r
            r +=1

        return maxProfit