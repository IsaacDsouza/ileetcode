#39. Combination Sum. Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res 
solution = Solution()
print(solution.combinationSum([2,3,6,7],7))