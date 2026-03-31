class Solution:
    def jump(self, nums: List[int]) -> int:
        def backtrack(i):
            if i >= len(nums)-1:
                return 0
            if nums[i]!=0:

                return 1+ min([backtrack(i+x) for x in range(1, nums[i]+1)])
            return 200000
        return backtrack(0) 

        