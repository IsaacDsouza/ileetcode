#383. Ransom Note. iven two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.Each ltter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}
        for c in magazine:
            if c not in counter:
                counter[c]=1
            else:
                counter[c]+=1
        
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c]==1:
                del counter[c]
            else:
                counter[c]-=1
        return True




solution=Solution()
print(solution.canConstruct("aa","aab"))