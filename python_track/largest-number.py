class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==nums.count(0):
            return str(0)
        for i in range(len(nums)):
            for j in range(1, len(nums)-i):
           
                str1 = str(nums[j-1])
                str2 = str(nums[j])
                if str2+str1 > str1+str2:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return "".join(map(str, nums))
     