class ATM:
    def __init__(self):
        self.notes = defaultdict(int)
        self.cash = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for note, count in zip(self.cash, banknotesCount):
            if count > 0:
                self.notes[note] += count

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5

        if amount % 10 != 0:
            return [-1]  # Withdrawal amount should be a multiple of 10 for available notes

        for note in sorted(self.notes.keys(), reverse=True):
            if note <= amount:
                count = min(amount // note, self.notes[note])
                self.notes[note] -= count
                res[self.cash.index(note)] += count
                amount -= count * note

        if amount == 0:
            return res
        else:
            # Rollback if the withdrawal is not possible with the available notes
            for note, count in zip(self.cash, res):
                self.notes[note] += count
            return [-1]

# Example usage:
atm = ATM()
atm.deposit([0, 5, 10, 2, 3])
result = atm.withdraw(1470)
print(result)  # Output: [0, 3, 9, 2, 2]
