from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        squares = defaultdict(set)
        n = len(board)

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".": continue
                if (num in row_seen[i] or
                    num in col_seen[j] or
                    num in squares[(i//3, j//3)]):
                    return False
                
                row_seen[i].add(num)
                col_seen[j].add(num)
                squares[(i//3, j//3)].add(num)
        return True
        
