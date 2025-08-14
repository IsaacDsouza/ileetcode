#53. Maximum Subarray. Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #Kadanes algo
        maxSub, curSum = nums[0], 0
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSub=max(maxSub, curSum)
        return maxSub

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))