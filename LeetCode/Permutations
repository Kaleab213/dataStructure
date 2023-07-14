class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(perm, visited):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in visited: continue
                visited.add(num)
                perm.append(num)
                backtracking(perm, visited)
                visited.remove(num)
                perm.pop()

        backtracking([], set())
        return res
