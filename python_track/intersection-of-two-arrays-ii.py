class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for val in count1:
            if val in count2:
                rep = min(count1[val], count2[val])
                for _ in range(rep):
                    res.append(val)
        return res
        