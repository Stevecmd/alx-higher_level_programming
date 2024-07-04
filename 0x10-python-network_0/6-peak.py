#!/usr/bin/python3
"""function to find peak in a list of unsorted integers."""


def find_peak_element(numbers):
    """
    Find a peak element in a list of unsorted integers.
    """
    if not numbers:
        return None

    start, end = 0, len(numbers) - 1

    while start < end:
        mid = (start + end) // 2
        if numbers[mid] > numbers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return numbers[start]
