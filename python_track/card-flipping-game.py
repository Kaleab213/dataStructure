class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        avoidset = set()
        for front, back in zip(fronts, backs):
            if front == back:
                avoidset.add(front)
        res = 2001
        for front, back in zip(fronts, backs):
            if front not in avoidset:
                res = min(res, front)
            if back not in avoidset:
                res = min(res, back)
        if res == 2001:
            return 0
        return res
        