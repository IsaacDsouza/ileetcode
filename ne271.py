#217. Encode and Decode Strings. Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res+= str(len(s))+'#'+s
        return res




    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res




solution = Solution()
a=solution.encode(["neet","code","love","you"])
print(solution.decode(a))
b=solution.encode(["we","say",":","yes"])
print(solution.decode(b))
