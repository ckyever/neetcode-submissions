"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalTuples = []
        for meeting in intervals:
            intervalTuples.append((meeting.start, meeting.end))

        intervalTuples.sort()

        for i in range(1, len(intervalTuples)):
            if intervalTuples[i][0] < intervalTuples[i-1][1]:
                return False

        return True
            