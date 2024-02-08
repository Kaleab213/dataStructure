class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            slow = fast = i
            is_forward = nums[slow] >= 0
            
            while True:
                slow = self.findNextIndex(nums, is_forward, slow)
                fast = self.findNextIndex(nums, is_forward, fast)
                if fast != -1:
                    fast = self.findNextIndex(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break
                    
            if slow == fast and slow != -1:
                return True
        return False
        
    
    def findNextIndex(self, arr, is_forward, index):
        direction = arr[index] >= 0
        if direction != is_forward:
            return -1
        next_index = (index+arr[index]) % len(arr)
        if next_index == index:
            return -1
        return next_index