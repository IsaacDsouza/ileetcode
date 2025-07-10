#402. Remove K Digits. Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        for n in num:
            while k>0 and stk and stk[-1]>n:
                stk.pop()
                k-=1
            stk.append(n)
        
        #if k remaining e.g(1234)
        stk=stk[:len(stk)-k]
        #convert to str and remove leading zeroes
        res="".join(stk).lstrip("0")
        return res if res else "0"
    
solution=Solution()
print(solution.removeKdigits("10200",1))