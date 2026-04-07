class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = nums.copy()
        for i in range(1,len(nums)):
            prefixSum[i] = prefixSum[i]+prefixSum[i-1]
        for i in range(len(prefixSum)):
            currDiff = prefixSum[-1]-prefixSum[i]
            if  currDiff== prefixSum[i-1] or (currDiff==0 and i == 0):
                return i
        
        return -1


        