#1029. Two City Scheduling. A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti. Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        diffs=[]
        for ca, cb in costs:
            diffs.append([cb-ca,ca,cb])
        diffs.sort()
        
        res=0
        for i in range(len(diffs)):
            if i<len(diffs)//2:
                res+=diffs[i][2]
            else:
                res+=diffs[i][1]
        return res

solution=Solution()
print(solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))