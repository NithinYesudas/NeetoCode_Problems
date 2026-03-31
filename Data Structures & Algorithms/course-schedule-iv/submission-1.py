from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        res = []
        mem = {}
        def dfs(preReq,course):
            if (preReq,course) in mem:
                return mem[(preReq,course)]
            if preReq in graph[course]:
                mem[(preReq,course)] = True
                return True
            for val in graph[course]:
                if dfs(preReq,val):
                    mem[(preReq,course)] = True
                    return True
            mem[(preReq,course)] = False
            return False

        for preReq,course in queries:
            if dfs(preReq,course):
                res.append(True)
            else:
                res.append(False)
        return res
                

        