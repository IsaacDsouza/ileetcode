#7. Reverse Integer. Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            sign=1
        else:
            sign=-1
        
        x=abs(x)
        s=str(x)

        rev_s=s[::-1]

        x=int(rev_s)
        res=sign*x


        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

solution = Solution()
print(solution.reverse(-123))