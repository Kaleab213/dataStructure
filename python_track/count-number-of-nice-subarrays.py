class Solution(object):
    def numberOfSubarrays(self, nums, k):

        pre_odd_count = {}
        pre_count = 0
        res = 0
        for num in nums:
            if num % 2 == 1:
                pre_count += 1
                pre_odd_count[pre_count] = 1
            else:
                pre_odd_count[pre_count] = pre_odd_count.get(pre_count, 0) + 1

            if pre_count == k:
                res += pre_odd_count.get(0, 0) + 1
            else:
                res += pre_odd_count.get(pre_count - k, 0)

        return res
                
