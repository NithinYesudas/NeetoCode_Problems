class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        mem = {}
        def dp(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i+j == len(s3):
                return True
            res = False
            if len(s1)>i and s1[i] == s3[i+j]:
                res = dp(i+1,j)
            if len(s2)>j and s2[j] == s3[i+j]:
                res = dp(i,j+1) or res
            mem[(i,j)] = res
            return res
        return dp(0,0)