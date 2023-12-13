class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = 1
        y = n
        while y < len(nums):
            val = nums.pop(y)
            nums.insert(x, val)
            y+=1
            x+=2
        return nums