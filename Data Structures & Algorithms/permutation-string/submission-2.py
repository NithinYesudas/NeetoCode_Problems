from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count = Counter(s1)
        length = len(s1)
        for i in range(length,len(s2)+1):
            curr_window = s2[i-length:i]
            print(curr_window)
            if count == Counter(curr_window):
                return True
        return False


        