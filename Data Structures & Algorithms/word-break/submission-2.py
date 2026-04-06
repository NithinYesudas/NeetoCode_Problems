class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet= set(wordDict)
        mem = {}
        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i == len(s):
                return True
            if j==len(s):
                return False
            res = False
            if s[i:j+1] in wordSet:
                res = dfs(j+1,j+1)
            res = dfs(i,j+1) or res
            mem[(i,j)] = res
            return res
        return dfs(0,0)
