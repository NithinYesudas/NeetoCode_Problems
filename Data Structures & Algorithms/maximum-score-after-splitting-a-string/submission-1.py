class Solution:
    def maxScore(self, s: str) -> int:
        leftScore = [0]*(len(s)+1)
        rightScore = [0]*(len(s)+1)
        for i in range(1,len(leftScore)):
            if s[i-1] == "0":
                leftScore[i]+=1
            leftScore[i]+=leftScore[i-1]
        for i in range(len(rightScore)-2,-1,-1):
            print(i)
            if s[i]=="1":
                rightScore[i]+=1
            rightScore[i]+=rightScore[i+1]
        maxSum = 0
        print(leftScore)
        print(rightScore)
        for i in range(1,len(leftScore)-1):
            maxSum= max(maxSum, leftScore[i]+rightScore[i])
        return maxSum

