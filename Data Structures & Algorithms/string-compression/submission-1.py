class Solution:
    def compress(self, chars: List[str]) -> int:
        k = i = 0
        n = len(chars)
        while i<n:
            chars[k]=chars[i]
            k+=1
            j = i+1
            while j<n and chars[j]==chars[i]:
                j+=1
            if j-i>1:
                for char in str(j-i):
                    
                    chars[k]=char
                    k+=1
            i=j
        return k
       