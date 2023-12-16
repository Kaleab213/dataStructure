class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for idx, val in count.items():
            res += val-1
        return len(s)-res
    