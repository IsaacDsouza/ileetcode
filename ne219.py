#219. Contains Duplicate II. Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1],3))
print(solution.containsNearbyDuplicate([1,0,1,1],1))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],2))


