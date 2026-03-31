class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res=0
        prefix = 0
        for i in range(0,len(nums)):
            prefix +=nums[i]
            diff = prefix-k
            
            res+=prefixSum.get(diff,0)
           
            prefixSum[prefix] = prefixSum.get(prefix,0)+1
      

            
     
            
            
        return res

        