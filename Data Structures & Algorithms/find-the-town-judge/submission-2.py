from collections import Counter, deque

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0]*n
        outdegree = [0]*n
        for a,b in trust:
            graph[a].append(b)
            indegree[a-1]+=1
            outdegree[b-1]+=1
        print(outdegree)
        print(indegree)
        print(graph)
        for i in range(1,n+1):
            if i not in graph and indegree[i-1]==0 and outdegree[i-1]==n-1:
                
                return i
        return -1
