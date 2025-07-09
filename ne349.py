#349. Intersection of Two Arrays. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        res=[]

        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res

solution = Solution()
print(solution.intersection([9,4,9,8,4],[4,9,5]))