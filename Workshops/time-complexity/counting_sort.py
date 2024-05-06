#!/usr/bin/python3

def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    # Initialize a list to count the occurrences of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array using the count array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
        print(sorted_arr)

    return sorted_arr


nums = [2, 1, 5, 4, 3]
print("Numbers to be sorted", nums)
sorted_nums = counting_sort(nums)
print("Sorted numbers:", sorted_nums)
