#345. Reverse Vowels of a String. Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        vow=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s=list(s)
        while l<r:
            if s[l] not in vow:
                l+=1
            elif s[r] not in vow:
                r-=1
            else:
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                l+=1
                r-=1
        return ''.join(s)