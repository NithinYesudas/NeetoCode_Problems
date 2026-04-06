class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def dfs(i,j):
            if i == len(word1) and j==len(word2):
                return 0
            val = 0
            if (i,j) in mem:
                return mem[(i,j)]
            if j==len(word2):
                val = len(word1)-i
            elif i == len(word1):
                val= len(word2)-j
            elif word1[i]==word2[j]:
                val = dfs(i+1,j+1)
            else:
                
                val = min(1+dfs(i,j+1), 1+dfs(i+1,j),1+dfs(i+1,j+1))
            mem[(i,j)] = val
            return val
        return dfs(0,0)


            
        