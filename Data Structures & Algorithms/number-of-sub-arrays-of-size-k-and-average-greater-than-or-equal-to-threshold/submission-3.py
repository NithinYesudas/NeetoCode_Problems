class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]*(len(arr)+1)
        for i in range(1, len(prefixSum)):
            prefixSum[i] = arr[i-1]+prefixSum[i-1]
        left = 0
        res = 0

        for i in range(k,len(prefixSum)):
            if (prefixSum[i]-prefixSum[left])/k >=threshold:
                res+=1
            left+=1

        return res





