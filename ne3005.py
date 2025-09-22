#3005. Count Elements With Maximum Frequency. You are given an array nums consisting of positive integers. Return the total frequencies of elements in nums such that those elements all have the maximum frequency. The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter={}
        for n in nums:
            if n not in counter:
                counter[n]=1
            else:
                counter[n]+=1
        
        freq=max(counter.values())
        count=0
        
        for f in counter.values():
            if f==freq:
                count+=f
        return count

solution = Solution()
print(solution.maxFrequencyElements([1,2,2,3,1,4]))