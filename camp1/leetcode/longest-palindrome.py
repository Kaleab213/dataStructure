class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd_added = False
        for keyy in count:
            if count[keyy]%2==1 and not odd_added:
                res += 1
                odd_added = True
            if count[keyy] >= 2:
                res += (count[keyy]//2)*2
        return res
