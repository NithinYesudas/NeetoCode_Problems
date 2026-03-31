class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,currPath,currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            if i>=len(nums) or currSum>target:
                return
            currPath.append(nums[i])
            helper(i,currPath,currSum+nums[i])
            currPath.pop()
            helper(i+1,currPath,currSum)
        helper(0,[],0)
        return res

        