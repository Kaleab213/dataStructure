class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        stack = []
        for i in range(n):
            if not stack:
                if nums[i] == 0:
                    return False
                stack.append(nums[i]+i)
            elif stack[-1] <= nums[i]+i:
                if nums[i] == 0 and i!=n-1:
                    return False
                else:
                    stack.append(nums[i]+i)
            if stack[-1]>=n:
                return True
        return True
