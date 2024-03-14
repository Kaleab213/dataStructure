class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for idx in range(len(nums)):
            val = target - nums[idx]

            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2

                if nums[mid]<=val:
                    left = mid+1
                else:
                    right = mid-1

            if right>=idx:
                res += 2**(right-idx)
        return res%(10**9+7)