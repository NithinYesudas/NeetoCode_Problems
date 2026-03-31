class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        max_string = ""
        for i in range(len(s)):
            left = i
            right = i
            while left>-1 and right < len(s):
                if s[left]==s[right]:
                    curr_string = s[left:right+1]
                    max_string = curr_string if max(len(curr_string),len(max_string)) == len(curr_string) else max_string
                    left-=1
                    right+=1
                else:
                    break
            left = i
            right = i+1
            while left>-1 and right < len(s):
                if s[left]==s[right]:
                    curr_string = s[left:right+1]
                    max_string = curr_string if max(len(curr_string),len(max_string)) == len(curr_string) else max_string
                    left-=1
                    right+=1
                else:
                    break
        return max_string

            