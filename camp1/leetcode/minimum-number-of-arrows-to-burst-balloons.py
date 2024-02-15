class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        red = 0
        for idx in range(1, len(points)):
            i, j = points[idx]
            previ, prevj = points[idx-1]
            if i >= previ and i <= prevj:
                red += 1
                points[idx][0] = max(i, previ)
                points[idx][1] = min(j, prevj)
        res = len(points)-red
        return res