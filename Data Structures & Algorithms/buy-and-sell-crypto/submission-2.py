class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        j=0
        for i in range(1,len(prices)):
            if prices[j]<prices[i]:
                max_profit=max(max_profit,prices[i]-prices[j])
            else:
                j=i
        return max_profit
            
            
        