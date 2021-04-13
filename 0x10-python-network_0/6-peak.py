#!/usr/bin/python3
""" This module contains class Rectangle """


def find_peak(list_of_integers):

    int left, right:
    mid = (left + right) // 2

    # check if the middle element is greater than its neighbors
    if ((mid == 0 or A[mid - 1] <= A[mid]) and
            (mid == len(A) - 1 or A[mid + 1] <= A[mid])):
        return mid

    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and A[mid - 1] > A[mid]:
        return findPeakElement(A, left, mid - 1)

    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return findPeakElement(A, mid + 1, right)


if __name__ == '__main__':
