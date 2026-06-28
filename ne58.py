#58. Length of Last Word. Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length=0
        i=len(s)-1

        while i>=0 and s[i]==' ':
            i-=1
        while i>=0 and s[i]!=' ':
            i-=1
            length+=1
        return length