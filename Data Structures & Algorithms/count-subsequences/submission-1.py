class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        mem = {}
        def dfs(i,j):
            if j == t_len:
                return 1
            if i>=s_len:
                return 0
            if (i,j) in mem:
                return mem[(i,j)]
            res = 0
            if s[i]==t[j]:
                res+=dfs(i+1,j+1)
            res+=dfs(i+1,j)
            mem[(i,j)] = res
            return res
        return dfs(0,0)

            
            

        