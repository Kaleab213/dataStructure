class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[0])):
                if rowidx+2<len(grid) and colidx+2<len(grid[0]):
                    total = grid[rowidx][colidx]+grid[rowidx][colidx+1]+grid[rowidx][colidx+2]+grid[rowidx+1][colidx+1]+grid[rowidx+2][colidx]+grid[rowidx+2][colidx+1]+grid[rowidx+2][colidx+2]
                    res = max(res, total)
        return res
