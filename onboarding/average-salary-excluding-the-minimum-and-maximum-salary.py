class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        total = sum(salary)
        small = min(salary)
        large = max(salary)
        return (total-small-large)/(n-2)