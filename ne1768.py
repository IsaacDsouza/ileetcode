#1768. Merge Strings Alternately. You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        min_l=min(m,n)
        ans=""
        for i in range(min_l):
            ans=ans+word1[i]+word2[i]
        if m>n:
            ans+=word1[min_l:]
        else:
            ans+=word2[min_l:]
        return ans
