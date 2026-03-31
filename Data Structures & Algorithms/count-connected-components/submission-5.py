class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for item in graph[node]:
                dfs(item)
            return True
        for key in range(n):
            if dfs(key):
                count+=1
        return count


        