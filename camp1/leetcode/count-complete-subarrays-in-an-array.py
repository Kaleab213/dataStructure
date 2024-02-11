class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, target = len(nums), len(set(nums))
        res = 0
        c = {}
        i = j = 0
        while j < n:
            c[nums[j]] = c.get(nums[j], 0) + 1
            while len(c) == target:
                c[nums[i]] -= 1
                if not c[nums[i]]:
                    del c[nums[i]]
                i += 1
                res += n - j
            j += 1
        return res