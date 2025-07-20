#739. Daily Temperatures. Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res=[0]*len(temperatures)
        stack=[] #(temp,index)pairs

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd]=i-stackInd
            stack.append((t,i))
        return res
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))