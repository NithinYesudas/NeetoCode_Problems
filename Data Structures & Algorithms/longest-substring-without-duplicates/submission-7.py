class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        a = {}
        left = 0
        length = 0
        for i in range(len(s)):

            if s[i] in a:
                length = max(length,i-left)
                temp = a[s[i]]+1
                for k in range(left,temp):
                    del a[s[k]]
                left = temp
            a[s[i]] = i
        length = max(length,(i+1)-left)
        return length

        

        