class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        current_length =1
        max_length = 1
        current_sign = 0
        for i in range(1,len(arr)):
            if current_sign == 0:
                if arr[i]>arr[i-1]:
                    current_sign=-1
                    current_length+=1
                elif arr[i]<arr[i-1]:
                    current_sign=1
                    current_length+=1

            elif current_sign==1:
                if arr[i]>arr[i-1]:
                    current_sign= -1
                    current_length+=1
                elif arr[i]<arr[i-1]:
                    current_sign=1
                    current_length=2
                else:
                    current_length=1
                    current_sign=0
            else:
                if arr[i]<arr[i-1]:
                    current_sign= 1
                    current_length+=1
                elif arr[i]>arr[i-1]:
                    current_sign=-1
                    current_length=2
                else:
                    current_sign=0
                    current_length=1
            max_length=max(max_length,current_length)
        return max_length


            