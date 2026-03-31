from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mem = {}
        res = []
        freq = Counter(nums)
        queu = []
        for key,value in freq.items():
            heapq.heappush(queu,(value,key))
            if len(queu)>k:
                heapq.heappop(queu)
        return [value[1] for value in queu ]
        for num in nums:
            mem[num] = mem.get(num,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        for key,val in mem.items():
            bucket[val].append(key)
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res

        