#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self,nums: [int]) ->bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
solution=Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3]))
print(solution.containsDuplicate([1,2,2,3,1]))


