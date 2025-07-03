#You're given expressions like "2/6+2/6" and need to:

 #  Parse the two fractions.

  #  Add them.

   # Simplify the result.

   # Return the simplified result as strings like "2/3".
class Solution:
    def addFractions(self, fractions:str)->str:
        results = []

        for expr in fractions:
            parts = expr.split('+')
            
            # Start with the first fraction
            num, den = map(int, parts[0].split('/'))
            total_num = num
            total_den = den

            for part in parts[1:]:
                num, den = map(int, part.split('/'))

                # Add the current fraction to the total
                total_num = total_num * den + num * total_den
                total_den = total_den * den

                # Inline GCD (Euclidean algorithm)
                a, b = total_num, total_den
                while b != 0:
                    a, b = b, a % b
                gcd = a

                # Reduce the fraction
                total_num //= gcd
                total_den //= gcd

            results.append(f"{total_num}/{total_den}")

        return results
solution = Solution()
fractions = [
    "722/148+360/176",
    "978/1212+183/183",
    "358/472+301/417",
    "780/309+684/988",
    "258/840+854/686"
]
print(solution.addFractions(fractions))

