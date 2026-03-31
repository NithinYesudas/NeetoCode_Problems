class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = [0]*len(nums)
        for i in range(len(nums)):
            pos = (i+k)%len(nums)
            nums2[pos] = nums[i]
        for i in range(len(nums2)):
            nums[i] = nums2[i]

        