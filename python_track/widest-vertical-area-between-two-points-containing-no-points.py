class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for idx in range(1, len(points)):
            width = points[idx][0]-points[idx-1][0]
            res = max(res, width)
        return res
