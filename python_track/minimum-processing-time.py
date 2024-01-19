class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        idx = len(tasks)-1
        res = 0
        for processor in processorTime:
            val = processor + tasks[idx]
            res = max(res, val)
            idx -= 4
        return res


