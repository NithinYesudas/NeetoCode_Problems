class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        i  = 0
        while i < len(bills):
            if bills[i] == 5:
                five+=1
            elif bills[i] == 10:
                ten+=1
                if five==0:
                    return False
                else:
                    five-=1
            else:
                if (ten == 0 and five < 3) or five==0:
                    return False
                elif ten > 0:
                    ten-=1
                    five-=1
                else:
                    five-=3
                
            i+=1
        return True
        
                    
        