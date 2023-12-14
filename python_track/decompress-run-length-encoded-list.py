class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        idx = 1
        while idx<len(nums):
            res += [nums[idx]]*nums[idx-1]
            idx+=2
        return res
        