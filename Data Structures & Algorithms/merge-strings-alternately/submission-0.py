class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str3 = ''
        l=r=0
        for i in range(len(word1)+len(word2)):
            if l<len(word1):
                if i%2==0 or r>=len(word2):
                    str3+=word1[l]
                    l+=1 
            if r<len(word2):
                if  i%2==1 or l>=len(word1):
                    str3+=word2[r]
                    r+=1
        return str3
             
        