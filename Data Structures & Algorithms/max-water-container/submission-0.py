class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(heights)-1
        while i < j:
            vol = min(heights[i],heights[j])*(j-i)
            max_vol = max(max_vol, vol)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_vol
        