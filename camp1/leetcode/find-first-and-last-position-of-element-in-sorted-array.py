class Solution:
    def searchRange(self, nums, target):
        val1 = bisect_left(nums, target)
        val2 = bisect_right(nums, target)
        if not nums or val1>=len(nums) or val1<0 or nums[val1] != target:
            val1, val2 = -1, 0
        return [val1, val2-1]
              