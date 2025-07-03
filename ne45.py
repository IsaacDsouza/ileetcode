#45. Jump Game II

class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        l,r=0,0

        while r<len(nums):
            farthest=0
            for i in range(l, r+1):
                farthest= max(farthest, i+nums[i])
            l=r+1
            r=farthest
            jumps+=1
        return jumps


solution = Solution()
print(solution.jump([2,3,1,1,4]))