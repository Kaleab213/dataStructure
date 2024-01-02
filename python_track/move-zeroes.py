class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        for i in range(count[0]):
            nums.remove(0)
            nums.append(0)
        return nums
        