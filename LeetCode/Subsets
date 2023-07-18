class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(subset, idx):
            res.append(subset.copy())
            if len(res) == 2**len(nums):
                return

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtracking(subset, i+1)
                subset.pop()

        backtracking([], 0)
        return res
