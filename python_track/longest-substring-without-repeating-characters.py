class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif  len(s) == 1:
            return 1

        array = list(s)
        maxi = 0

        for i in range(len(s)):
            news = ""
            for j in range(i, len(s)):
                if array[j] not in news:
                    news+=array[j]
                    maxi = max(maxi, len(news)) 
                else:
                    break
        return maxi