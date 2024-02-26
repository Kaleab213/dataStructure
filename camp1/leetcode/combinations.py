class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        def recursive(cand, curr):
            if len(cand) == k:
                self.res.append(cand.copy())
                return

            for idx in range(curr,n+1):
                cand.append(idx)
                recursive(cand, idx+1)
                cand.pop()

        recursive([], 1)
        return self.res