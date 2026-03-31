class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                left = i
                right = j
                isPalindrome = True
                while left<=right:
                    if s[left]!=s[right]:
                        isPalindrome = False
                    left+=1
                    right-=1
                if isPalindrome:
                    res+=1
        return res
        