class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res =res+ word+"|"
        
        return res

    def decode(self, s: str) -> List[str]:
        
        res = s.split("|")
        res.pop()
        return res
