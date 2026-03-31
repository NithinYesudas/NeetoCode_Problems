class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1,len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
        return l+1

        