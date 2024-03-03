class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        
        def recursive(curr, idx):
            total = sum(curr)
            if total == target:
                self.res.append(curr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] > target:
                    break
                
                curr.append(candidates[i])
                recursive(curr, i + 1)
                curr.pop()

        recursive([], 0)
        return self.res
