class Solution:
    def totalNQueens(self, n: int) -> int:

        def isSafe(row, col, queens):
            for r, c in queens:
                if r == row or c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtrack(row, queens):
            if row == n:
                self.res += 1
                return
                
            for col in range(n):
                if isSafe(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens)
                    queens.pop()

        self.res = 0
        backtrack(0, [])
        return self.res
