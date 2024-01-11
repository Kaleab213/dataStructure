class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_ = [1 if letter in 'aeiou' else 0 for letter in s]
        total = sum(s_[:k])
        maximum = total
        for i in range(len(s_)-k):
            total += s_[i+k] - s_[i]
            if total > maximum:
                maximum = total
        return maximum