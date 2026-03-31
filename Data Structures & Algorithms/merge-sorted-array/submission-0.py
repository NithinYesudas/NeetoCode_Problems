class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_len= len(nums1)-len(nums2)
        for i in range(nums1_len,len(nums1)):
            nums1[i]=nums2[i-nums1_len]
        nums1.sort()
        return nums1
       
        