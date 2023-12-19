class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                tempolong = 1
                val = num
                while val+1 in nums:
                    tempolong += 1
                    val+=1
                res = max(res, tempolong)
        return res