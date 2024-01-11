class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        n = len(nums)
        start = 0
        while start<n and not nums[start]:
            start += 1
        end = start
        fzero = None
        res = 0
        while end<n:
            if not nums[end]:
                if not fzero:
                    fzero = end
                else:
                    res = max(res, end-start-1)
                    start = fzero+1
                    fzero = end
            end += 1
        if fzero:
            res = max(res, end-start-1)
        else:
            res = max(res, end-start)
        return res
               