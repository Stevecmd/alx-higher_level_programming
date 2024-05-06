#!/usr/bin/python3

def selection_sort(arr):
    n = len(arr)

    for curr_index in range(n - 1):
        smallest_index = curr_index
        for possible_smallest in range(curr_index + 1, n):
            if arr[possible_smallest] < arr[smallest_index]:
                    smallest_index = possible_smallest

        # swapping
        arr[curr_index], arr[smallest_index] = arr[smallest_index], arr[curr_index]
        print(arr)

    return arr


nums = [8, 5, 3, 1, 4]
print("Numbers to be sorted", nums)
selection_sort(nums)
