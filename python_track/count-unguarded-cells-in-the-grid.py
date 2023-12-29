class Solution:
    def __init__(self):
        self.guardedcell = set()
        self.wallset = set()
        self.guardset = set()

    def northguard(self, x, y, m, n):
        while y >= 0 and (x,y) not in self.wallset and (x,y) not in self.guardset:
            self.guardedcell.add((x,y))
            y -= 1

    def southguard(self, x, y, m, n):
        while y < n and (x,y) not in self.wallset and (x,y) not in self.guardset:
            self.guardedcell.add((x,y))
            y += 1

    def eastguard(self, x, y, m, n):
        while x >= 0 and (x,y) not in self.wallset and (x,y) not in self.guardset:
            self.guardedcell.add((x,y))
            x -= 1

    def westguard(self, x, y, m, n):
        while x < m and (x,y) not in self.wallset and (x,y) not in self.guardset:
            self.guardedcell.add((x,y))
            x += 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        self.wallset = set(map(tuple, walls))
        self.guardset = set(map(tuple, guards))
        for gx, gy in guards:
            self.northguard(gx, gy-1, m, n)
            self.southguard(gx, gy+1, m, n)
            self.eastguard(gx-1, gy, m, n)
            self.westguard(gx+1, gy, m, n)

        res = 0
        for row in range(m):
            for col in range(n):
                if (row,col) not in self.guardedcell and (row,col) not in self.wallset and (row,col) not in self.guardset:
                    res += 1
        return res
