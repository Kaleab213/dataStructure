class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(mygoal):
            n = len(nums)
            left = 0
            right = 0
            total = 0
            res = 0
            while right < n:
                if total==mygoal and nums[right]:
                    while left<n and nums[left]==0:
                        left += 1
                    left += 1
                    total -= 1
                    if left>=n:
                        break
                if total<=mygoal:
                    res += right-left+1
                total += nums[right]
                right += 1
            return res

        val1 = helper(goal)
        val2 = helper(goal-1)
        return val1-val2
        