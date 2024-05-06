#!/usr/bin/python3

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        is_swapped = False
        for j in range(n - i):
            if j + 1 < n and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
                print(arr)
                if not is_swapped:
                    break


return arr

nums = [2, 1, 5, 4, 3]
print("Numbers to be sorted", nums)
bubble_sort(nums)
