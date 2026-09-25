class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_med = set()
        neg_med = set()
        res = []
        board = [["."]*n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(copy) for copy in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos_med or (r-c) in neg_med:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                pos_med.add(r+c)
                neg_med.add(r-c)
                backtrack(r+1)
                board[r][c] = '.'
                cols.remove(c)
                pos_med.remove(r+c)
                neg_med.remove(r-c)
        backtrack(0)
        return res
        