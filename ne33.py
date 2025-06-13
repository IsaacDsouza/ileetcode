#33. Search in Rotated Sorted Array. There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums:list[int], target:int)->int:
        l, r = 0, len(nums)-1

        while l<=r:
            m=(l+r)//2

            if nums[m]==target:
                return m
            
            #left sorted part
            if nums[l]<=nums[m]: #means it checks if the left side has sorted elements(in asc)
                if target>nums[m]:
                    l=m+1
                elif target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            #right sorted part
            else:#if left is not sorted in asc order we go to the right side
                if target<nums[m]:
                    r=m-1
                elif target>nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1
    
solution=Solution()
print(solution.search([4,5,6,7,0,1,2],3))
print(solution.search([4,5,6,7,0,1,2],0))
print(solution.search([7,0,1,2,4,5,6],0))
print(solution.search([7,0,1,2,4,5,6],5))







