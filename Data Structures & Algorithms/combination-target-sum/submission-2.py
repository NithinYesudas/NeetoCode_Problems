class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,currPath,currSum):
            if currSum>target or i>=len(nums):
                return
            if currSum == target and currPath not in res:
                res.append(currPath.copy())
            currPath.append(nums[i])
            helper(i,currPath,nums[i]+currSum)
            currPath.pop()
            helper(i+1,currPath,currSum)
        helper(0,[],0)
        return res

        