"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import unittest


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MinHeap:

    def __init__(self):
        self.heap = []
        self.sorted_list = []

    def get_parent(self, i):
        return (i-1)//2

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def push(self, val):

        if val is None:
            return

        if len(self.heap) < 1:
            return self.heap.append(val)
        else:
            self.heap.append(val)

            i = len(self.heap) - 1
            self.perc_up(i)

    def perc_up(self, index):

        while index > 0:

            parent = self.get_parent(index)

            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

            index -= 1

    def pop(self):

        # ! Look into using deque and heapq here instead
        # Save lowest item in array in sorted list array
        self.sorted_list.append(self.heap[0])

        #  swap last element with first element and pop the lowest element
        # once we do that, we have to perc_down to restore heap property
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()

        self.perc_down(0)

    def perc_down(self, index):

        while True:
            left = self.get_left_child(index)
            right = self.get_right_child(index)

            smallest = index

            if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
                smallest = left
            elif right < len(self.heap) and self.heap[smallest] > self.heap[right]:
                smallest = right

            if smallest != index:

                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]

                index = smallest
            else:
                break


def sort_k_lists(lists):
    pass


class TestSortKLists(unittest.TestCase):

    def test_ll_are_being_sorted(self):
        pass
