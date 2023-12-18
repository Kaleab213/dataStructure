class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for num, val in count.items():
            if val > len(nums)/3:
                res.append(num)
        return res