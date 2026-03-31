from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        queu = []
        for key,value in freq.items():
            heapq.heappush(queu,(value,key))
            if len(queu)>k:
                heapq.heappop(queu)
        return [value[1] for value in queu ]
        