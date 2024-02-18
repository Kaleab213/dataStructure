class RecentCounter:
    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        idx = bisect.bisect_right(self.req, t)
        self.req.insert(idx, t)
        if t-3000<0:
            return len(self.req[:idx+1])
        flr = bisect.bisect_left(self.req, t-3000)
        return len(self.req[flr:idx+1])
