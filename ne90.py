#90. Subsets II. Given an integer array nums that may contain duplicates, return all possible subsets(the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i,subsets):
            if i==len(nums):
                res.append(subsets.copy())
                return
            
            #to include nums[i]
            subsets.append(nums[i])
            backtrack(i+1, subsets)
            subsets.pop()

            #to exclude nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1, subsets)

        backtrack(0,[])
        return res

solution = Solution()
print(solution.subsetsWithDup([1,2,2]))