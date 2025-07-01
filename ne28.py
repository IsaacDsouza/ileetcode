#28. Find the Index of the First Occurrence in a String. Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        for i in range(len(haystack)+1-len(needle)):
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
                if j==len(needle)-1:
                    return i
        return -1
solution = Solution()
print(solution.strStr("sadbutsad","but"))