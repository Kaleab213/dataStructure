class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = target
        res = 0
        while curr > 1:
            if maxDoubles > 0:
                if curr%2 == 0:
                    curr = curr/2
                    maxDoubles -= 1
                else:
                    curr -= 1
                res += 1
            else:
                res += curr-1
                curr = 1
        return int(res)