#213. House Robber II. You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.robLine(nums[1:]), self.robLine(nums[:-1]))
    
    def robLine(self, nums: list[int])-> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1=rob2
            rob2=temp
        return rob2
solution=Solution()
print(solution.rob([2,3,2]))