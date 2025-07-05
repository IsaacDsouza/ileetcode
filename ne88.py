#88. Merge Sorted Array. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        x, y= m-1, n-1

        for z in range(len(nums1)-1, -1, -1):
            if x<0:
                nums1[z]=nums2[y]
                y-=1
            elif y<0:
                break
            elif nums1[x]>nums2[y]:
                nums1[z]=nums1[x]
                x-=1
            else:
                nums1[z]=nums2[y]
                y-=1

        return nums1
solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
        