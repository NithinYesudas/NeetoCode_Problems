class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[right]< nums[mid]:
                left = mid+1
            else:
                right = mid
        pivot = left
        def binary_search(left, right):
            while left<=right:
                mid = (left+right) //2
                if nums[mid] == target:
                    return mid
                if target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        res = binary_search(0,pivot-1)
        if res!=-1:
            return res
        return binary_search(pivot,len(nums)-1)
