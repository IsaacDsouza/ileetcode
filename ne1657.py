#1657. Determine if Two Strings Are Close. Two strings are considered close if you can attain one from the other using the following operations: Operation 1: Swap any two existing characters. For example, abcde -> aecdb Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character. For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's) You can use the operations on either string as many times as necessary. Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1)!=len(word2):
            return False
        
        if set(word1)!=set(word2):
            return False
        
        counter1, counter2 = {}, {}

        for c in word1:
            if c not in counter1:
                counter1[c]=1
            else:
                counter1[c]+=1
        
        for c in word2:
            if c not in counter2:
                counter2[c]=1
            else:
                counter2[c]+=1
        
        return sorted(counter1.values())==sorted(counter2.values())