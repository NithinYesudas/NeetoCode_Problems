class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_length = 0
        for i,num in enumerate(nums):
            if i>max_length:
                return False
            if max_length >=len(nums)-1:
                return True
            max_length = max(max_length,i+num)
        

        