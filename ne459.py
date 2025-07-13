#459. Repeated Substring Pattern. Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ds=(s+s)[1:-1]
        return s in ds

solution = Solution()
print(solution.repeatedSubstringPattern("abcabcabcabc"))