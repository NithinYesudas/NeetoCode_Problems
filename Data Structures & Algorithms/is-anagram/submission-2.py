class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        if len(s)!=len(t):
            return False
        mem= {}
        for char in s:
            if char in mem:
                mem[char]+=1
            else:
                mem[char] = 1
        for char in t:
            if char not in mem or mem[char]==0:
                return False
            mem[char]-=1
        return True
        