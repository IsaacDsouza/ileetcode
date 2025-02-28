#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi=0
        mini=prices[0]
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            maxi=max(maxi,prices[i]-mini)
        return maxi

solution=Solution()
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([7,1,5,3,6,4]))
