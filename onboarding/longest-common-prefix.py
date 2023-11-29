from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            val = strs[0][i]
            print(val)
            is_diff = True
            for j in range(len(strs)):
                if len(strs[j])<=i or strs[j][i]!=val:
                    is_diff = False
                    break
            if not is_diff:
                break
            res += val
        return res
