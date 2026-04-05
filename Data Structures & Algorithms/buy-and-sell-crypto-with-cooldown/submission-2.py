class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}
        def dfs(l,r):
            if l >=len(prices) or r>=len(prices):
                return 0
            if (l,r) in mem:
                return mem[(l,r)]
            if prices[r]>prices[l]:
                mem[(l,r)] =max(prices[r]-prices[l]+dfs(r+2,r+2),dfs(l,r+1))
                
            else:
                mem[(l,r)] = dfs(r,r+1)
            return mem[(l,r)]
        return dfs(0,0)

        