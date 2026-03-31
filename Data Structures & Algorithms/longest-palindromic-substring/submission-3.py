class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        max_length = ""
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
                    curr_string = s[i:j+1]
                    max_length = curr_string if max(len(max_length),len(curr_string)) == len(curr_string) else max_length
        return max_length

        