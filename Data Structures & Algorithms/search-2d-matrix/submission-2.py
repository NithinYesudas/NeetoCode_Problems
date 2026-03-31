class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        top = 0
        bottom = len(matrix) - 1
        
        # Step 1: Find the correct row
        while top <= bottom:
            mid = (top + bottom) // 2
            
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break   # target must be in this row
        
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        
        # Step 2: Binary search inside the row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
