#875. Koko Eating Bananas. Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return. Return the minimum integer k such that she can eat all the bananas within h hours.

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def k_works(k)->bool:
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            return hours<=h
        
        l,r = 1, max(piles)

        while l<r:
            k=(l+r)//2
            if k_works(k):
                r=k
            else:
                l=k+1
        return r
solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))