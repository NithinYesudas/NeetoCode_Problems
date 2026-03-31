class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left+right)//2
            if self.isShippable(weights,mid,days):
                print(mid)
                right=mid-1
            else:
                left=mid+1
        return left
    def isShippable(self,weights,capacity,days):
        currSum =0
        for i in range(len(weights)):
            currSum+=weights[i]
            if currSum>capacity:
                days-=1
                currSum=weights[i]
            elif currSum==capacity:
                days-=1
                currSum=0
        if currSum>0:
            days-=1
        if days<0:
            return False
        else:
            return True


        