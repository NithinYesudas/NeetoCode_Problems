from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = set()
        steps = 0
        def dfs(i):
            nonlocal steps
            if i in visited or i>=n:
                return
            visited.add(i)
            curr = hasApple[i]
            for item in tree[i]:
               if dfs(item):
                        steps += 2
                        curr = True
            
            return curr
        dfs(0)
        return steps
            
        

        