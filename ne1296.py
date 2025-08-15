#1296. Divide Array in Sets of K Consecutive Numbers. Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers. Return true if it is possible. Otherwise, return false.

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        count={}
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1
        nums.sort()
        for num in nums:
            if count[num]:
                for i in range(num, num+k):
                    if i not in count or count[i]==0:
                        return False
                    count[i]-=1
        return True 
solution = Solution()
print(solution.isPossibleDivide([1,2,3,3,4,4,5,6],  4))