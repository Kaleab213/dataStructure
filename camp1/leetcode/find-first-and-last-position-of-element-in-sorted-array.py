class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        left = 0
        right = len(nums)-1
        while left<=right:

            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid-1
            else:
                left = mid+1

        if left>=len(nums) or nums[left]!=target:
            return [-1,-1]
        res.append(left)

        left = 0
        right = len(nums)-1
        while left<=right:

            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1
            else:
                left = mid+1

        if right<0 or nums[right]!=target:
            return [-1,-1]
        res.append(right)

        return res
