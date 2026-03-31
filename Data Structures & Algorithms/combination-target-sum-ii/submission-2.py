class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(i,currPath,currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            if i >= len(candidates) or currSum > target:
                return 
            
            currPath.append(candidates[i])
            helper(i+1,currPath,currSum+candidates[i])
            currPath.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            helper(j,currPath,currSum)
        helper(0,[],0)
        return res