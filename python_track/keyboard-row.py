class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        key = ["qQWwEeRrTtYyUuIiOoPp","aAsSdDfFgGhHjJkKlL", "ZzXxCcVvBbNnMm"]
        for word in words:
            for i in range(3):
                add = True
                for letter in word:
                    if letter not in key[i]:
                        print(letter, key[i])
                        add = False
                        break
                if add:
                    res.append(word)
                    break
        return res

        