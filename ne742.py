#724. Find Pivot Index. Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array. Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=0
        for i in range(len(nums)):
            total+=nums
        
        l_total=0

        for i in range(len(nums)):
            r_total=total-l_total-nums[i]

            if r_total==l_total:
                return i
            
            l_total+=nums[i]
        return -1