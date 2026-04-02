from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        minHeight = float('inf')
        res = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(i):
            visited.add(i)
            maxDepth = 0
            for neighbor in graph[i]:
                if neighbor not in visited:
                    maxDepth = max(1+dfs(neighbor),maxDepth)
            return maxDepth
        for i in range(n):
            visited = set()
            height = dfs(i)
            if height<minHeight:
                res.clear()
                res.append(i)
                minHeight=height
            elif height==minHeight:
                res.append(i)
        return res
        