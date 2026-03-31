from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges):
            return True
        if n-1 != len(edges):
            return False
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for item in graph[node]:
                dfs(item)
        dfs(edges[0][0])
        if len(visited) ==n:
            return True
        return False
        
        

        