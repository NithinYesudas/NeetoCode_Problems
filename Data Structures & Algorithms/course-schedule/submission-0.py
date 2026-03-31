from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for crs, pre in prerequisites:
            graph[crs].append(pre)
            indegree[crs]+=1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] ==0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            for key, value in graph.items():
                if node in value:
                    value.remove(node)
                    indegree[key]-=1
                    if indegree[key]==0:
                        q.append(key)
            res.append(node)
        if len(res) != numCourses:
            return False
        return True
                

            
        