
import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        pq=[]
        for i, (p, t) in enumerate(classes):
            curPr=p/t
            newPr=(p+1)/(t+1)
            heapq.heappush(pq, (-(newPr-curPr), i))
        
        while extraStudents>0:
            gain, i = heapq.heappop(pq)
            classes[i][0]+=1
            classes[i][1]+=1

            p,t = classes[i]
            curPr=p/t
            newPr=(p+1)/(t+1)
            heapq.heappush(pq, -(newPr-curPr))
            extraStudents-=1
        ans = sum(p/t for p, t in classes)
        return ans/len(classes)
solution = Solution()
print(solution.maxAverageRatio([[1,2],[3,5],[2,2]], 2))