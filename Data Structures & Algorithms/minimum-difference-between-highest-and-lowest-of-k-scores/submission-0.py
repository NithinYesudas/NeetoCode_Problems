class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDifference = float('inf')
        left = 0
        for i in range(k-1,len(nums)):
            minDifference = min(minDifference, nums[i]-nums[left])
            left+=1
        return minDifference


        