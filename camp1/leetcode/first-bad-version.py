# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        bad = n+1
        while left <= right:
            res = (left+right)//2
            if isBadVersion(res):
                right = res-1
                bad = res
            else:
                left = res+1
        return bad
        