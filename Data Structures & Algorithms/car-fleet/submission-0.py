class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos,spd) for pos, spd in zip(position,speed)]
        pairs.sort(reverse=True)
        recentTime = 0
        count=0
        for pair in pairs:
            pos,spd = pair
            timeNeeded = (target-pos)/spd
            if timeNeeded>recentTime:
                count+=1
                recentTime=timeNeeded
        return count
        