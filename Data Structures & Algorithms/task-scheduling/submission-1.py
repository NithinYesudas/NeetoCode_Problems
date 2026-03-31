from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-val for val in freq.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while len(heap) or q:
            time+=1
            if len(heap):
                a = heapq.heappop(heap)
                a+=1

                if a<0:
                    q.append((a,n+time))
            if time > n:
                if q and q[0][1] == time:
                    num, time = q.popleft()
                    heapq.heappush(heap,num)
        return time







        