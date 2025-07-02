#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l
    
solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))