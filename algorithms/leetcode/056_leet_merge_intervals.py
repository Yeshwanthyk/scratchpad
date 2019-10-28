"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
import unittest


def merge_intervals(intervals):

    if (len(intervals) <= 1):
        return intervals

    intervals = sorted(intervals, key=lambda i: i[0])
    updated_intervals = []

    for i in range(0, len(intervals), 2):

        if intervals[i+1][0] <= intervals[i][1]:
            tmp = []
            while(intervals[i] and intervals[i+1]):
                if (intervals[i][0] <= intervals[i+1][0]):
                    tmp.append(intervals[i][0])
                    intervals[i].pop(0)
                else:
                    tmp.append(intervals[i+1][0])
                    intervals[i+1].pop(0)

            tmp = tmp + intervals[i] + intervals[i+1]
            updated_intervals.append([tmp[0], tmp[len(tmp) - 1]])
        else:
            updated_intervals.append(intervals[i])
            updated_intervals.append(intervals[i+1])

    return updated_intervals


intervals = [[1, 4], [2, 3]]
ans = merge_intervals(intervals)
print(ans)


# class TestMergeIntervals(unittest.Testcase):
#     def test_merge_interval_works():
#         intervals = [[1, 4], [4, 5]]
#         self.assert(merge_intervals(intervals), [[1, 5]])


# if __name__ == '__main__':
#     unittest.main()
