import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        mid=0
        while left<=right:
            mid = (left+right)//2
            if self.isEatable(piles,mid,h):
                right=mid-1
            else:
                left=mid+1
        return left
    def isEatable(self,piles,k,h):
        for pile in piles:
            timeNeeded = math.ceil(pile/k)
            h-=timeNeeded
        if h<0:
            return False
        else:
            return True
        