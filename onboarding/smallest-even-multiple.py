class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        temp = n
        while True:
            if n%2==0 and n%temp==0:
                return n
            n+=1
        