class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(len(nums)):
            if not nums[i]:
                res = max(res, count)
                count = 0
            else:
                count += 1
        res = max(res, count)
        return res
        