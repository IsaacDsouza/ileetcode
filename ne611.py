#611. Valid Triangle Number. Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        c = 0
        for i in range(len(nums)-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    c += r - l
                    r -= 1
                else:
                    l += 1
        return c

solution = Solution()
print(solution.triangleNumber([2,2,3,4]))