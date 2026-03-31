class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gasLeft = 0
            for j in range(len(gas)):
                pos = (i+j)%len(gas)
                gasLeft+=gas[pos]
                if gasLeft<cost[pos]:
                    break
                gasLeft-=cost[pos]
                if pos == (i-1)%len(gas):
                    return i
        return -1
        


        