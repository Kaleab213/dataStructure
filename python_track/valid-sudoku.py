class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rowidx in range(len(board)):
            visited = set()
            for colidx in range(len(board[0])):
                val = board[rowidx][colidx]
                if val in visited and val != ".":
                    return False
                visited.add(val)

        for colidx in range(len(board[0])):
            visited = set()
            for rowidx in range(len(board)):
                val = board[rowidx][colidx]
                if val in visited and val != ".":
                    return False
                visited.add(val)

        def subboxfinder(row, col):
            visited = []
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] in visited and board[row+i][col+j]!=".":
                        return False
                    visited.append(board[row+i][col+j])
            return True

        for rowidx in range(0,8,3):
            for colidx in range(0,8,3):
                if not subboxfinder(rowidx, colidx):
                    return False
        return True


