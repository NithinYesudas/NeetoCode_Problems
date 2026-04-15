class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        minOperation = float('inf')
        operations = 0
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                operations+=1
            if (i-left)+1 == k:
                minOperation = min(minOperation,operations)
                if blocks[left]=='W':
                    operations-=1
                left+=1
        return minOperation

        