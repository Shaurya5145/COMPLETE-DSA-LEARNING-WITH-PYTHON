class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])

        removed_count = 0
        prev_end = intervals[0][1]

        n = len(intervals)

        for i in range(1,n):
            if intervals[i][0] < prev_end:
                removed_count+=1

            else:
                prev_end = intervals[i][1]

        return removed_count
