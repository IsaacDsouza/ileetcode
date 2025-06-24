#40. Combination Sum II. Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total>target or i==len(candidates):
                return
            
            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            #exclude candidates[i]
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            dfs(i+1, cur, total)

        dfs(0,[],0)
        return res 
solution = Solution()
print(solution.combinationSum([10,1,2,7,6,1,5],8))