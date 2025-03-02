#1291. An integer has sequential digits if and only if each digit in the number is one more than the previous digit. Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        d = "0123456789"
        res = set()
        a = len(str(low))
        b = len(str(high))
        while a<=b:
            for i in range(len(d)-a+1):
                ans=d[i:i+a]
                if low<=int(ans)<=high:
                    res.add(int(ans))
            a+=1
        return list(sorted(res))

solution=Solution()
print(solution.sequentialDigits(100, 300))
print(solution.sequentialDigits(1000, 13000))