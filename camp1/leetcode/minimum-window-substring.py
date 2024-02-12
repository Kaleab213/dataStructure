class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        window = defaultdict(int)
        count = 0
        min_length = float('inf')
        result_left = 0
        result_right = 0

        for char in t:
            target[char] += 1

        left = 0
        for right in range(len(s)):
            
            if s[right] in target:
                window[s[right]] += 1
                if window[s[right]] <= target[s[right]]:
                    count += 1

            while count == len(t):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result_left = left
                    result_right = right

                if s[left] in target:
                    window[s[left]] -= 1
                    if window[s[left]] < target[s[left]]:
                        count -= 1
                left += 1

        if min_length == float('inf'):
            return ""
        else:
            return s[result_left:result_right+1]

                
                 