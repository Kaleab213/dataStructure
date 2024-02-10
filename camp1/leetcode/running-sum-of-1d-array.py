class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        res = []
        for num in nums: 
            total += num
            res.append(total)
        return res
