#14.Longest Common Prefix. Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=""

        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
    
solution= Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))