#46. Permutations. Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, perms = [], []

        def backtrack():
            if len(perms)==len(nums):
                res.append(perms.copy())
                return
            
            for n in nums:
                if n not in perms:
                    perms.append(n)
                    backtrack()
                    perms.pop()
        backtrack()
        return res
solution = Solution()
print(solution.permute([1,2,3]))