#209. Minimum Size Subarray Sum. Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total+=nums[r]
            if total>=target:
                res=min(r-l+1, res)
                total-=nums[l]
                l+=1
        return 0 if res==float('inf') else res
solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
