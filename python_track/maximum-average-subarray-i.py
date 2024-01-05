class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        ma = max(P[i+k] - P[i] 
                for i in xrange(len(nums) - k + 1))
        return ma / float(k)
        