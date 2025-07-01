#1514. Path with Maximum Probability. You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i]. Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability. If there is no path from start to end, return 0


import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append([src, succProb[i]])
        visit=set()
        maxheap=[(-1,start_node)]

        while maxheap:
            prob, cur = heapq.heappop(maxheap)
            visit.add(cur)

            if cur==end_node:
                return prob*-1
            
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(maxheap,(prob*edgeProb, nei))
        return 0
solution = Solution()
print(solution.maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.3], 0,2))
