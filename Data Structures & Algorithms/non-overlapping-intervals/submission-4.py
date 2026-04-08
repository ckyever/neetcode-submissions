class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval:(interval[0], interval[1]))
        deletedIntervals = 0

        previousStart, previousEnd = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            currentStart, currentEnd = intervals[i][0], intervals[i][1]

            if currentStart >= previousEnd:
                previousStart, previousEnd = currentStart, currentEnd
            else:
                deletedIntervals += 1
                previousStart, previousEnd = currentStart, min(previousEnd, currentEnd)

        return deletedIntervals
        
