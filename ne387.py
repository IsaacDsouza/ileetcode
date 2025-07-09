#387. First Unique Character in a String. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter={}
        for c in s:
            if c not in counter:
                counter[c]=1
            else:
                counter[c]+=1
        
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1


solution=Solution()
print(solution.firstUniqChar("loveleetcode"))