class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        closest = []
        for i in range(n):
            closest.append((points[i][0]**2+points[i][1]**2, points[i]))
        heapq.heapify(closest)
        res = []
        for i in range(k):
            _, val = heapq.heappop(closest)
            res.append(val)
        return res

            