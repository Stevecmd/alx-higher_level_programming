#!/usr/bin/python3

def insertion_sort(arr):
    n = len(arr)

    # Iterate over the array starting from the second element
    for curr_index in range(1, n):
        # Store the current element to be inserted
        key = arr[curr_index]
        # Start from the element just before the current element
        j = curr_index - 1
        # Move elements of arr[0..curr_index-1],
        # that are greater than key, to one position ahead of
        # their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key at its correct position in sorted order
        arr[j + 1] = key
        # Print the array after each step
        print(arr)

    return arr


nums = [8, 5, 3, 1, 4]
print("Numbers to be sorted", nums)
insertion_sort(nums)
