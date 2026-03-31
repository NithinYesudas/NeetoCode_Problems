class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        mem={}
        for i in range(len(s)):
            for j in range(i,len(s)):
                if (i,j) in mem and mem[(i,j)]:
                    res+=1
                    continue
                left = i
                right = j
                isPalindrome = True
                while left<=right:
                    if s[left]!=s[right]:
                        isPalindrome = False
                    left+=1
                    right-=1
                    mem[(i,j)] = isPalindrome
                if isPalindrome:
                    
                    res+=1
        return res
        