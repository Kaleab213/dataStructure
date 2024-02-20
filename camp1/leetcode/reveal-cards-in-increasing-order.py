class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        queue = deque()
        for i in range(len(deck)):
            queue.append(i) 
        
        result = [0] * len(deck)
        for card in deck:
            idx = queue.popleft()
            result[idx] = card
            if queue:  
                queue.append(queue.popleft())
        return result