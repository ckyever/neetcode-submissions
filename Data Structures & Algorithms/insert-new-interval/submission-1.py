class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval
        addRemaining = False

        for start, end in intervals:
            if addRemaining:
                result.append([start, end])
                continue

            if newEnd < start:
                result.append([newStart, newEnd])
                result.append([start, end])
                addRemaining = True
            elif newStart > end:
                result.append([start, end])
                continue
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

        if not addRemaining:
            result.append([newStart, newEnd])

        return result