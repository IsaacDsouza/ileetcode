class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        prevMap = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
    
solution=Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
print(solution.twoSum(nums = [3,2,4], target = 6))
print(solution.twoSum(nums = [3,3], target = 6))