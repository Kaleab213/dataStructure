class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        for i in nums:
            if i >= target:
                return 1

        if sum(nums) < target:
            return 0

        length = len(nums)+1
        i = 0
        j = 0
        mysum = nums[i]

        while j < len(nums):
            if i == j:
                j+=1
                if j < len(nums):
                    mysum += nums[j]
            elif mysum >= target:
                length = min(length, j-i+1)
                mysum -= nums[i]
                i += 1
            else:
                j += 1
                if j < len(nums):
                    mysum += nums[j]
        return length
    