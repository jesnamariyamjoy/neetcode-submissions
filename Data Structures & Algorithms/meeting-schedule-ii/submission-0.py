"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        s = 0
        e = 0
        active_rooms = 0
        max_rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                active_rooms += 1
                max_rooms = max(max_rooms, active_rooms)
                s += 1
            else:
                active_rooms -= 1
                e += 1

        return max_rooms