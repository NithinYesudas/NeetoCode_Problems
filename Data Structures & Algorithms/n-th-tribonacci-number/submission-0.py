class Solution:
    def __init__(self):
        self.mem = {}
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n == 2:
            return 1
        if n in self.mem:
            return self.mem[n]
        self.mem[n]= self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.mem[n]
        