class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        idx = []
        for i in range(n*2):
            if i >= n:
                i -= n
            while stack and stack[-1] < nums[i]:
                stack.pop()
                temp = idx.pop()
                res[temp] = nums[i]
            stack.append(nums[i])
            idx.append(i)
        return res


