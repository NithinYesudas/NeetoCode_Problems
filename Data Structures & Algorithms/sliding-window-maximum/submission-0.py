import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        for r in range(k,len(nums)+1):
            print(nums[left:r])
            a = heapq.nlargest(1,nums[left:r])
            print(a)
            res.append(a[0])
            left+=1
        return res
        
