class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            curr_one = 0
            curr_value = i

            while curr_value:
                curr_one+=curr_value%2
                curr_value=curr_value>>1
            res.append(curr_one)
        return res
        