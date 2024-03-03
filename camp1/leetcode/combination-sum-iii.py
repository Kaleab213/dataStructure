class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        def recursive(curr, idx):
            if sum(curr)>n or sum(curr)==n and len(curr)<k:
                return 

            if len(curr)==k:
                if sum(curr)==n:
                    self.res.append(curr.copy())
                return

            for i in range(idx, 10):
                curr.append(i)
                recursive(curr, i+1)
                curr.pop()

        recursive([], 1)
        return self.res
