#5.  Longest Palindromic Substring.Given a string s, return the longest palindrome in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=0
        res=""

        for i in range(len(s)):
            #odd length
            l,r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            #even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
solution = Solution()
print(solution.longestPalindrome("babad"))