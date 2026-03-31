import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = [[-a,'a'],[-b,'b'], [-c,'c']]
        heapq.heapify(heap)
        prev = None
        res=''
        while heap:
            freq, letter = heapq.heappop(heap)
            if freq==0:
                continue
            res+=letter
            freq+=1
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if freq<0:
                if len(res)>=2 and res[-2]==letter:
                    prev=[freq,letter]
                else:
                    heapq.heappush(heap,[freq,letter])

        return res
        
            

            