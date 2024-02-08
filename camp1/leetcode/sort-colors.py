class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        return nums
