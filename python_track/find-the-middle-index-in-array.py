class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return 0
        # if len(nums)==2:
        #     if nums[1]==0:
        #         return 0
        #     if nums[0]==0:
        #         return 1

        total = sum(nums)
        currsum = 0
        for idx in range(len(nums)):
            if total-currsum-nums[idx]==currsum:
                return idx
            currsum += nums[idx]
        return -1
        