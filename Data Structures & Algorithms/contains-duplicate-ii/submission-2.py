from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in mem:
                for index in mem[nums[i]]:
                    if abs(i-index) <=k:
                        return True
            mem[nums[i]].append(i)
        
        return False
        