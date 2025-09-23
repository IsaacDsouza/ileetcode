class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevImap = {}
        n=len(nums)
        for i in range(n):
            complement=target-nums[i]
            if complement in prevImap:
                return [prevImap[complement], i]
            prevImap[nums[i]]=i
        
        
        return []
    
solution=Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
print(solution.twoSum(nums = [3,2,4], target = 6))
print(solution.twoSum(nums = [3,3], target = 6))