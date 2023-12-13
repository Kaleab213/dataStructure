class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i in range(len(nums)):
            value = target - nums[i]
            if value in my_dict and i != my_dict[value]:
                return [i, my_dict[value]]
        