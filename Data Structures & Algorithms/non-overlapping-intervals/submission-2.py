class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed= 0
        print(intervals)
        for i, item in enumerate(intervals):
            if i+1 <len(intervals) and intervals[i+1][0] < item[1]:
                intervals[i+1] = item
                removed+=1
        return removed
        