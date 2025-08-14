#152. Maximum Product Subarray. Given an integer array nums, find a that has the largest product, and return the product. The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res=nums[0]
        curMin, curMax = 1, 1
        
        for num in nums:
            tmp = num * curMax
            curMax = max(num*curMax, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res=max(res, curMax)
        return res

solution = Solution()
print(solution.maxProduct([2,3,-2,4]))