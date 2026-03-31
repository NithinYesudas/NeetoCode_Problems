import math,heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest= []
        for point in points:
            a = (point[0])**2
            b = (point[1])**2
            distance = math.sqrt(a+b)
            heapq.heappush(closest,[distance,point])
        res = []
        for i in range(k):
            a = heapq.heappop(closest)
            res.append(a[1])
        return res
