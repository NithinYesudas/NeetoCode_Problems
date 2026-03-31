class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        res = []
        for num in nums:
            mem[num] = mem.get(num,0)+1
        for i in range(k):
            maxVal = 0
            max_key = 0
            for key, value in mem.items():
                if key in res:
                    continue
                maxVal = max(maxVal,value)
                if maxVal == value:
                    max_key = key
            res.append(max_key)
        return res

        