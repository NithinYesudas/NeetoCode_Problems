class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = [0]*(len(nums)+1)
        for i in range(1,len(prefixSum)):
            prefixSum[i]= prefixSum[i-1]+nums[i-1]
        for i in range(2,len(prefixSum)):
            for j in range(0,(i-2)+1):
                if (prefixSum[i]-prefixSum[j])%k==0:
                    return True
        return False
        