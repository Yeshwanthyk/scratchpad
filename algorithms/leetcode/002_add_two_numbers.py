"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


def add_two_numbers(A, B):

    if not A and not B:
        return []

    summed = []
    # Pad smaller array with 0s
    max_len = max(len(A), len(B))

    if len(A) < len(B):
        for i in range(len(B) - len(A)):
            A.append(0)
    else:
        for i in range(len(A) - len(B)):
            B.append(0)

    # iterate over the length of same sized arrays and minus 10. Add the value to new
    # list and add next set of values with 1
    carry = 0
    for i in range(max_len):
        new_sum = carry + A[i] + B[i]
        if (new_sum >= 10):
            summed.append((10 - new_sum))
            carry = 1
        else:
            summed.append(new_sum)
            carry = 0

    return summed


A = [2, 4, 3]
B = [5, 6, 4]
ans = add_two_numbers(A, B)
print(ans)
