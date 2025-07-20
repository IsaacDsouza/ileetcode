#22. Generate Parentheses. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack=[]
        res=[]

        def backtrack(openn, closed):
            if openn==closed==n:
                res.append(''.join(stack))
                return

            if openn<n:
                stack.append('(')
                backtrack(openn+1, closed)
                stack.pop()
            if closed<openn:
                stack.append(')')
                backtrack(openn,closed+1)
                stack.pop()
        backtrack(0,0)
        return res

solution = Solution()
print(solution.generateParenthesis(3))