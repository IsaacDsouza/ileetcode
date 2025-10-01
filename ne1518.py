#1518. Water Bottles. There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle. The operation of drinking a full water bottle turns it into an empty bottle. Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        extra = 0
        while numBottles > 0:
            ans += numBottles
            empty = numBottles + extra
            numBottles = empty // numExchange
            extra = empty % numExchange
        return ans
solution = Solution()
print(solution.numWaterBottles(9,3))