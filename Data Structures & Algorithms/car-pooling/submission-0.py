class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        minHeap = []
        currSize = 0
        for item in trips:
            numPass, start, end = item
            while len(minHeap) and minHeap[0][0]<=start:
                currSize-=minHeap[0][1]
                heapq.heappop(minHeap)
            currSize+=numPass
            heapq.heappush(minHeap,[end,numPass])
            if currSize>capacity:
                return False
        return True

        
        