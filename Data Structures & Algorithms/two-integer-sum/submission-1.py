class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            currDiff = target -nums[i]
            if currDiff in mem:
                return [mem[currDiff],i]
            else:
                mem[nums[i]] = i
        