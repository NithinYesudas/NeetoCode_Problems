from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = [-1.0]*len(queries)
        graph = defaultdict(list)
        weight = {}
        for (a,b), value in zip(equations,values):
            graph[a].append(b)
            graph[b].append(a)
            weight[(a,b)] = value
            weight[(b,a)] = 1/value
        visited = set()
        def dfs(curr,target, value):
            if target == curr:
                return value
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    res = dfs(neighbour,target,value*weight[(curr,neighbour)])
                    if res!=-1:
                        return res
            return -1

        for i in range(len(queries)):
            a,b = queries[i]
            if a not in graph or b not in graph:
                result[i]=-1
            else:
                visited=set()
                result[i]=dfs(a,b,1)
        return result

        