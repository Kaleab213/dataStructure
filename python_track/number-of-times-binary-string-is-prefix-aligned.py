class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxidx = 0
        res = 0
        for idx in range(len(flips)):
            maxidx = max(maxidx, flips[idx])
            if maxidx == idx+1:
                res += 1
        return res
        