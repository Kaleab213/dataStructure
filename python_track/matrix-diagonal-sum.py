class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for row in range(len(mat)):
            for col in range(len(mat)):
                if row-col == 0 or row+col == len(mat)-1:
                    res += mat[row][col]
        return res
                
        