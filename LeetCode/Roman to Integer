class Solution:
    def romanToInt(self, s: str) -> int:

        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if len(s) == 1:
            return dict[s[0]]

        i = 0
        sum = 0
        while i < len(s):
            if i == len(s) - 1:
                sum += dict[s[i]]
            elif dict[s[i]] >= dict[s[i+1]]:
                sum += dict[s[i]]
            elif dict[s[i]] < dict[s[i+1]]:
                sum -= dict[s[i]]
            i+=1
        return sum
