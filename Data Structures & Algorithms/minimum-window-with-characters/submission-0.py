from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = {}
        left = 0
        min_count = float('inf')
        res = ""
        for r in range(len(s)):
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r],0)+1
            print(s_count)
            while all(s_count.get(c,0) >= t_count[c] for c in t_count):
                print(s[left:r+1])
                min_count = min(min_count, (r+1)-left)
                if min_count == (r+1)-left:
                    res = s[left:r+1]
                if s[left] in s_count:
                    s_count[s[left]]-=1
                left+=1
        return res





            


                






        