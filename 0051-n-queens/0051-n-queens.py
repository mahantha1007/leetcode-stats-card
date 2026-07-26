class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r+c) in diag1 or (r-c) in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c); diag1.add(r+c); diag2.add(r-c)
                backtrack(r+1)
                board[r][c] = "."
                cols.remove(c); diag1.remove(r+c); diag2.remove(r-c)

        backtrack(0)
        return res
