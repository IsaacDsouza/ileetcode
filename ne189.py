#189. Rotate Array. Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: list[int], k: int) -> list:
        k=k%len(nums)

        def rev(l,r,num):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        rev(0,len(nums)-1,nums)
        rev(0,k-1,nums)
        rev(k,len(nums)-1,nums)
        return nums
solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7],3))
