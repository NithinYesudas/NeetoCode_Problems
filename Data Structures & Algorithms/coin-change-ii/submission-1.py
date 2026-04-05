class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def dfs(i,currSum):
            if currSum == amount:
                return 1
            if i>=len(coins) or currSum>amount:
                return 0
            if (i,currSum) in mem:
                return mem[(i,currSum)]
            mem[(i,currSum)] = dfs(i,currSum+coins[i])+dfs(i+1,currSum)
            return mem[(i,currSum)]
        return dfs(0,0)

        