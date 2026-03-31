class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(32):
            if n%2 == 1:
                res+="1"
            else:
                res+="0"
            n=n>>1
        return int(res,2)
       