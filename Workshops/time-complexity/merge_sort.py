#!/usr/bin/python3

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)

    print(sorted_arr)  # Print the array after each merge step

    return sorted_arr


def merge(left_half, right_half):
    sorted_arr = []
    left_index = 0
    right_index = 0

    # Merge the two halves into a single sorted array
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_arr.append(left_half[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_half[right_index])
            right_index += 1

    # Append remaining elements from left_half
    while left_index < len(left_half):
        sorted_arr.append(left_half[left_index])
        left_index += 1

    # Append remaining elements from right_half
    while right_index < len(right_half):
        sorted_arr.append(right_half[right_index])
        right_index += 1

    return sorted_arr


nums = [8, 5, 7, 2, 3, 6, 1, 4]
print("Numbers to be sorted", nums)
sorted_nums = merge_sort(nums)
print("Sorted numbers:", sorted_nums)
