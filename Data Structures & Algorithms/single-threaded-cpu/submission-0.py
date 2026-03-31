import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, item in enumerate(tasks):
            item.append(i)
        tasks.sort()
        res = []
        heap = []
        i=0
        time = tasks[0][0]
        while heap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not heap:
                time = tasks[i][0]
            else:
                processTime, index = heapq.heappop(heap)
                time+=processTime
                res.append(index)
        return res


            


        

        
        