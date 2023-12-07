class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        steps = 0
        for i in range(1, len(points)):
            xpath = abs(points[i][0] - points[i-1][0])
            ypath = abs(points[i][1] - points[i-1][1])
            steps += max(xpath, ypath)
        return steps
        