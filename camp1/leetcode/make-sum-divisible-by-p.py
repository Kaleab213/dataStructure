class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        modulus = sum(nums)%p
        if modulus==0: return 0
            
        prefix_sum, ans = 0, len(nums)
        remainder_dict = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remain = prefix_sum%p
            temp = (remain-modulus)%p
            if temp in remainder_dict:
                ans = min(ans, i-remainder_dict[temp])
            remainder_dict[remain] = i
        return ans if ans<len(nums) else -1
