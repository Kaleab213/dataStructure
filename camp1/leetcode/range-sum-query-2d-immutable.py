class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n, m = len(matrix), len(matrix[0])

        self.ps = []
        for _ in range(n):
            self.ps.append([0]*m)

        for r in range(n):
            for c in range(m):
                self.psFinder(r, c)
    
    def psFinder(self, i, j):
        if i-1<0:
            self.ps[i][j] = self.ps[i][j-1]+self.matrix[i][j]
        elif j-1<0:
            self.ps[i][j] = self.ps[i-1][j]+self.matrix[i][j]
        else:
            self.ps[i][j] = self.ps[i-1][j]+self.ps[i][j-1]-self.ps[i-1][j-1]+self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr = self.ps[row2][col2]

        suml = 0
        if col1-1>=0:
            suml = self.ps[row2][col1-1]

        sumt = 0
        if row1-1>=0:
            sumt = self.ps[row1-1][col2]

        sumd = 0
        if row1-1>=0 and col1-1>=0:
            sumd = self.ps[row1-1][col1-1]

        return curr-suml-sumt+sumd

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)