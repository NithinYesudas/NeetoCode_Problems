class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1]]
        for i in range(1,numRows):
            curr = []
            prev = pascals[i-1]

            for j in range(i+1):
                print("i", i)
                print("j", j)
                if j== 0 or j==i:
                
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            pascals.append(curr)
        return pascals


        