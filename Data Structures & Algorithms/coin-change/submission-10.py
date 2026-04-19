class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem ={}
        def dfs(i,currSum):
            if currSum==amount:
                return 0
            if i>=len(coins) or currSum>amount:
                return float('inf')
            if (i,currSum) in mem:
                return mem[(i,currSum)]
            take = 1 + dfs(i,coins[i]+currSum)
            skip = dfs(i+1,currSum)
            mem[(i,currSum)]= min(take,skip)
            return mem[(i,currSum)]

        res = dfs(0,0)
        return res if res != float('inf') else -1

        