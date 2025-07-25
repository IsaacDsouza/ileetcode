#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxp=0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp, profit)
            else:
                l=r
            r+=1
        return maxp

solution=Solution()
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([7,1,5,3,6,4]))
