#128. Longest Consecutive Sequence Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums2=list(set(nums))
        nums2.sort()
        x=0
        maxi=-1
        print(nums2)
        for i in range(1,len(nums2)):
            if nums2[i-1]==nums2[i]-1:
                x+=1
            else:
                maxi=max(maxi,x)
                x=0

        return max(maxi,x)+1

solution=Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([1,0,1,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

