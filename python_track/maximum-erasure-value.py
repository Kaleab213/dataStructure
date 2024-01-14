class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        visited = set()
        res = 0
        totalsum = 0
        for right in range(len(nums)):
            if nums[right] not in visited:
                visited.add(nums[right])
                totalsum += nums[right]
            else:
                res = max(res, totalsum)
                while nums[left] != nums[right]:
                    visited.remove(nums[left])
                    totalsum -= nums[left]
                    left += 1
                left += 1
        res = max(res, totalsum)
        return res
            