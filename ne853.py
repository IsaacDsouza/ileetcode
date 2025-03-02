# 853. There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack=[]
        cars=[(p,s) for p ,s in zip(position,speed)]
        cars.sort(reverse=True,key=lambda x:x[0])
        print(cars)
        for i in range(len(cars)):
            p,s=cars[i]
            t=(target-p)/s
            stack.append(t)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)

solution=Solution()
print(solution.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
print(solution.carFleet(100,[0,2,4],[4,2,1]))