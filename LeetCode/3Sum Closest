class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            j = i + 1
            end = len(nums) - 1
            while j < end:

                current = nums[i] + nums[j] + nums[end]

                if abs(current-target) < abs(closest-target):
                    closest = current

                if current < target:
                    j += 1
                elif current > target:
                    end-=1
                else:
                    return current

        return closest
