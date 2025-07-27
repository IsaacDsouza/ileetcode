#1436. Destination City. You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city. It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        '''count={}
        for p in paths:
            count[p[0]]=p[1]
        a=set(count.values())
        b=set(count.keys())
        return list(a-b)[0]'''
        
        starts=set()
        for path in paths:
            starts.add(path[0])
        
        for path in paths:
            if path[1] not in starts:
                return path[1]

solution = Solution()
print(solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))