#20. Valid Parentheses. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def validParentheses(self, s:str)->bool:
        closePairs= {')':'(', '}':'{', ']':'['}
        stk = []

        for c in s:
            if c not in closePairs:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped!=closePairs[c]:
                        return False
        return not stk
solution=Solution()
print(solution.validParentheses("()"))
print(solution.validParentheses("(]"))
