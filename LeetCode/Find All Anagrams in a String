class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)-1
        result = []
        pattern_count = Counter(p)
        string_count = Counter(s[:m])
        for i in range(m, len(s)):
            string_count[s[i]] += 1
            if string_count == pattern_count:
                result.append(i - len(p) + 1)
            string_count[s[i - len(p) + 1]] -= 1
        return result
