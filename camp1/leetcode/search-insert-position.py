class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        return bisect_left(nums, target)
        # n = len(nums)
        # l, r = 0, n - 1
        # while l <= r:
        #     midd = (l + r) // 2
        #     if nums[midd] == target:
        #         return midd
        #     elif nums[midd] < target:
        #         l = midd + 1
        #     else:
        #         r = midd - 1
        # return l
