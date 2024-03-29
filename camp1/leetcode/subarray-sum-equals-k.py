class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		d = {0:1}
		cur_sum = 0
		res = 0
		for i in nums:
			cur_sum += i
			if cur_sum - k in d:
				res += d[cur_sum - k]
			if cur_sum not in d:
				d[cur_sum] = 1
			else:
				d[cur_sum] += 1            
		return res