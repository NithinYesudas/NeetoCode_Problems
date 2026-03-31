class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = {0: 1}
        right = {len(nums)-1: 1}
        output=[]

        for i in range(len(nums)-1):
            left[i+1] = left[i]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(len(nums)):
            output.append(left[i]*right[i])
        return output


        