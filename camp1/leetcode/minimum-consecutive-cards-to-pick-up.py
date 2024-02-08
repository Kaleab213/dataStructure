class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        store = set()
        res = len(cards)+1
        for right in range(len(cards)):
            if cards[right] in store:
                while cards[left]!=cards[right]:
                    store.remove(cards[left])
                    left += 1
                res = min(res, right-left+1)
                store.remove(cards[left])
                left += 1
            store.add(cards[right])
            right += 1
        if res == len(cards)+1:
            return -1
        return res
