"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


def trapping_rain_water(array):

    l1 = 0
    l2 = 1
    trapped = 0

    # move until we find an elevation
    while array[l1] == 0:
        l1 += 1
        l2 += 1

    while l2 < len(array):

        if array[l2] == 0:
            l2 += 1
        else:
            trapped += min(array[l1], array[l2]) * (l2 - l1)
            l1 = l2
            l2 = l2 + 1
    return trapped


array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = trapping_rain_water(array)
print(ans)
