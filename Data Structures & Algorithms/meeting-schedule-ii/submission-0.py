"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x : x.start)

        prevEndArr = [intervals[0].end]

        for interval in intervals[1:]:
            updated = False
            for i in range(len(prevEndArr)):
                if prevEndArr[i] <= interval.start:
                    prevEndArr[i] = interval.end
                    updated = True
                    break
            if not updated:
                prevEndArr.append(interval.end)
        
        return len(prevEndArr)

