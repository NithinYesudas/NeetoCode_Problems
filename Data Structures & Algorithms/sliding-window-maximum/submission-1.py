import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        for r in range(k,len(nums)+1):
            a = heapq.nlargest(1,nums[left:r])
            res.append(a[0])
            left+=1
        return res
        
