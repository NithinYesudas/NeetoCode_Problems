from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.post = defaultdict(list)
    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        self.post[userId].append([self.time,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following_list = self.following[userId]
        heap = []
        for follow in following_list:
            heap.extend(self.post[follow])
        heap.extend(self.post[userId])
        heapq.heapify(heap)
        res = []
        while len(res)<10 and len(heap):
            a = heapq.heappop(heap)
            res.append(a[1])
        return res
     
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId==followerId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        