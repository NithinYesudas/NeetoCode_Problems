from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
  
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        square_dict = defaultdict(set)
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if board[r][c]==".":
                    continue
                if curr in row_dict[r] or curr in column_dict[c] or curr in square_dict[(r//3,c//3)]:
                    return False
                row_dict[r].add(curr)
                column_dict[c].add(curr)
                square_dict[(r//3,c//3)].add(curr)
        return True



        
        

        