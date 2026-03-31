from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        occurence = Counter(s)
        heap =[]
        for key, val in occurence.items():
            heapq.heappush(heap,[-val,key])
        res=""
        prev= None
        while heap:
            freq, val = heapq.heappop(heap)
            
            res+=val
            freq+=1
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if freq<0:
                prev = [freq,val] 
        if prev:
            return ""
        return res
            



        