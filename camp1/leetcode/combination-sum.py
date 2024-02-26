class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def recursive(curr, idx):
            if sum(curr) == target:
                self.res.append(curr.copy())
                return
            if sum(curr) > target or idx>=len(candidates):
                return

            recursive(curr, idx+1)
            curr.append(candidates[idx])
            recursive(curr, idx)
            curr.pop()

        recursive([], 0)
        return self.res