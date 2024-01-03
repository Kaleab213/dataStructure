class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = float('inf')
        for num in nums1:
            if num in nums2:
                res = min(res, num)
        if res == float('inf'):
            return -1
        return res
