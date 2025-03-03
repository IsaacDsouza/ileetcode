#215. Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element. Can you solve it without sorting?
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        array = [-n for n in nums]
        heapq.heapify(array)
        for _ in range(k-1):
            heapq.heappop(array)
        return -heapq.heappop(array)

solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4],2))
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6],4))