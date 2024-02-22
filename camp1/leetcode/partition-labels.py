class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurrence = {char: index for index, char in enumerate(S)}
        start = end = 0
        partitions = []
        for i, char in enumerate(S):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions
