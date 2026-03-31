class Solution:
    def jump(self, nums: List[int]) -> int:
        min_length = 0
        def backtrack(i):
            if i >= len(nums)-1:
                return 0
            if nums[i]!=0:

                return 1+ min([backtrack(i+x) for x in range(1, nums[i]+1)])
            return 1
        return backtrack(0)

        