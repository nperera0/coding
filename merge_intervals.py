'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """


        if len(intervals) == 0: return []

        intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for session in intervals[1:]:
            if session[0] <=  merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], session[1])
            else:
                merged_intervals.append(session)


        return merged_intervals
