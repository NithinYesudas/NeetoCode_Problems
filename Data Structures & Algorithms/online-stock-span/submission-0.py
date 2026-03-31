class StockSpanner:

    def __init__(self):
        self.nums = []
        

    def next(self, price: int) -> int:
        span = 1
        r = len(self.nums)-1
        while r>-1 and self.nums[r]<=price:
            span+=1
            r-=1
        self.nums.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)