class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        val = num//3
        if (val-1)+val+(val+1) == num:
            return [val-1, val, val+1]
        return []
        