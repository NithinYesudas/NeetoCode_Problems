class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def helper(i,path):
            if i >=len(nums):
                return
            path.append(nums[i])
            res.append(path.copy())
            helper(i+1,path)
            path.pop()
            helper(i+1,path)
        helper(0,[])
        return res
        