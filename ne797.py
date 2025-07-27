#797. All Paths From Source to Target. Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order. The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        end=len(graph)-1

        def dfs(node, path, output):
            if node==end:
                output.append(path)
            
            for nx in graph[node]:
                dfs(nx, path+[nx], output)

        output=[]
        dfs(0,[0],output)
        return output

solution=Solution()
print(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))