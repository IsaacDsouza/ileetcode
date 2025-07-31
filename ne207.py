#207. Course Schedule. There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses. Otherwise, return false.


from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g=defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        
        unvisited, visiting, visited = 0, 1, 2
        states=[unvisited]*numCourses

        def dfs(node):
            if states[node]==visited:
                return True
            elif states[node]==visiting:
                return False

            states[node]=visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
                
            states[node]=visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

solution = Solution()
print(solution.canFinish(2, [[1,0],[0,1]]))
