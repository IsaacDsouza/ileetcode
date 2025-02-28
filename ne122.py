#122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi=0
        dp={}
        def dfs(i,hold):
            if i==len(prices):
                return 0
            if (i,hold) in dp:
                return dp[(i,hold)]
            if hold:
                dp[(i,hold)]=max(dfs(i+1,False)+prices[i],dfs(i+1,True))
            else:
                dp[(i,hold)]=max(dfs(i+1,True)-prices[i],dfs(i+1,False))
            return dp[(i,hold)]
        return dfs(0,False)

solution=Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))
