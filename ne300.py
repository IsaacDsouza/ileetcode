#300. Longest Increasing Subsequence. Given an integer array nums, return the length of the longest strictly increasing subsequence

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS=[1]*len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i], LIS[j]+1)
        return max(LIS)

solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))