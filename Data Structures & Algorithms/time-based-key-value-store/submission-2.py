from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mem = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        recentTimestamp = 0
        recentVal = ""
        for val, timstmp in self.mem[key]:
            if timestamp>=timstmp:
                recentTimestamp = max(recentTimestamp,timstmp)
                recentVal = val if max(recentTimestamp,timstmp)==timstmp else recentVal
                
        return recentVal

            
            

        return val
        
