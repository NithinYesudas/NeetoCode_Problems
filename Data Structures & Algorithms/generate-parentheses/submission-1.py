class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bactrack(opened,closed,curr):
            if opened ==0 and closed==0:
                res.append(curr)
                return
            if opened>0:
               bactrack(opened-1,closed,curr+'(')
            if closed>0 and opened<closed:
              bactrack(opened,closed-1,curr+')')
        bactrack(n,n,"")
        return res
            
            
        