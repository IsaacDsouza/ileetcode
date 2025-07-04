#647. Palindromic Substrings. Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        for i in range(len(s)):
            #for odd length
            l, r =i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            #for even length
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res




solution = Solution()
print(solution.countSubstrings("babad"))