class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1
                prev_end = min(prev_end, end)

        return removals