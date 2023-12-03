class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alien_dict = {c: i for i, c in enumerate(order)}

        def compare_words(word1, word2):
            for c1, c2 in zip(word1, word2):
                if alien_dict[c1] < alien_dict[c2]:
                    return True
                elif alien_dict[c1] > alien_dict[c2]:
                    return False
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare_words(words[i], words[i + 1]):
                return False

        return True
