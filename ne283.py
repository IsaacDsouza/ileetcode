#283. Move Zeroes. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j=0

        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j+=1
        return nums