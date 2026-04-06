class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]

            if newEnd < start:
                result.append([newStart, newEnd])
                return result + intervals[i:]
            elif newStart > end:
                result.append([start, end])
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

        result.append([newStart, newEnd])

        return result