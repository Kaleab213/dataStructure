class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        rem = x
        while rem >= 10:
            curr = rem%10
            res = res*10+curr
            rem = rem//10
        res = res*10+rem
        return x == res     
