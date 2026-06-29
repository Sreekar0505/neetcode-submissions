class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        ans = [intervals[0]]

        for start, end in intervals:
            prevEnd = ans[-1][1]

            if prevEnd >= start:
                ans[-1][1] = max(prevEnd, end)
            else:
                ans.append([start,end])
        
        return ans