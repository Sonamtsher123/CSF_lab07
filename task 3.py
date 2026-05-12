def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function
original_list = [9, 5, 1, 4, 3]
print(f"Original List: {original_list}")
sorted_list = insertion_sort(original_list.copy())
print(f"Sorted List: {sorted_list}")