import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        print(nums)
        for i in range(k-1):
            a =heapq.heappop(nums)
            print(a)
        return -nums[0]
        