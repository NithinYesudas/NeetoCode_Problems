class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dfs(i,currSum):
            if currSum == amount:
                return 0
            if i>=len(coins) or currSum > amount:
                return float('inf')
            if (i,currSum) in mem:
                return mem[(i,currSum)]
            take =1+dfs(i,currSum+coins[i])
            skip=dfs(i+1,currSum)
            
            res= min(take,skip)
            mem[(i,currSum)] = res
            return res
            
        result =  dfs(0,0)
        return -1 if result== float('inf') else result
            

            
            
        