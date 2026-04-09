"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval:interval.start)

        rooms = [[intervals[0]]]

        for current in intervals[1:]:
            foundRoom = False

            for room in rooms:
                if current.start >= room[-1].end:
                    room.append(current)
                    foundRoom = True
                    break
            
            if not foundRoom:
                rooms.append([current])
            
        return len(rooms)