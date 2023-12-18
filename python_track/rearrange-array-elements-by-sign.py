class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = 0
        neg = 0
        res = []
        while pos<n and neg<n:
            while (pos<n and nums[pos]<0) or (neg<n and nums[neg]>0):
                if pos<n and nums[pos] < 0:
                    pos += 1
                if neg<n and nums[neg] > 0:
                    neg += 1
            if pos<n:
                res.append(nums[pos])
                pos += 1
            if neg<n:
                res.append(nums[neg])
                neg += 1
        return res
        


        