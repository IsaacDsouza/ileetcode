#1207. Unique Number of Occurrences. Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        counter={}

        for c in arr:
            if c not in counter:
                counter[c]=1
            else:
                counter[c]+=1
        a=set(counter.values())
        
        if len(counter.values())>len(a):
            return False
        return True