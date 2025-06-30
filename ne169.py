#169. Majority Element. Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = nums[0]

        for i in range(len(nums)):
            if nums[i]==candidate:
                count+=1
            elif nums[i]!=candidate and count==0:
                candidate=nums[i]
                count+=1
            else:
                count-=1
        return candidate
    
solution=Solution()
print(solution.majorityElement([3,2,2,1,1,1,2,2,2,1]))