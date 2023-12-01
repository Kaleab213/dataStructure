class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1

        res = 0
        for num in my_dict:
            res += (my_dict[num] * (my_dict[num] - 1)) // 2
        return res
