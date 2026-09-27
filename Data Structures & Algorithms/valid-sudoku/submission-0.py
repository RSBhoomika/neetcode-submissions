class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                boxes_id = (r//3)*3 + (c//3)

                if val in rows[r] or val in cols[c] or val in boxes[boxes_id]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[boxes_id].add(val)
        return True
        