class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        ans = [intervals[0]]
        count = 0

        for start,end in intervals[1:]:
            prevEnd = ans[-1][1]
            if prevEnd > start:
                count+=1
                if ans[-1][0] == start:
                    ans[-1][1] = min(prevEnd,end)
                else:
                    if prevEnd <= end:
                        continue
                    else:
                        ans[-1] = [start,end]
            else:
                ans.append([start,end])

        return count