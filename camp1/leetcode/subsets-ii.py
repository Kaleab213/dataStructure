class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()  
        
        def backtracking(subset, idx):
            res.append(subset.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtracking(subset, i+1)
                subset.pop()
        
        backtracking([], 0)
        return res
