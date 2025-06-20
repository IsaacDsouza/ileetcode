#78. Subsets. Given an integer array nums of unique elements, return all possible(the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums:list[int])->list[list[int]]:
        res=[]

        subs=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subs.copy())
                return
            
            #to include nums[i]
            subs.append(nums[i])
            dfs(i+1)

            #to exclude nums[i]
            subs.pop()
            dfs(i+1)
        
        dfs(0)
        return res

solution = Solution()
print(solution.subsets([1,2,3]))