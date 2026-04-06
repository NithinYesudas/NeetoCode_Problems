class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            if n<0:
                max_prod,min_prod = min_prod,max_prod
            max_prod = max(n,n*max_prod)
            min_prod = min(n,n*min_prod)
            result = max(result,max_prod)
        return result