def insertion_sort_with_trace(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}: {arr}")
    return arr

# Test the function
original_list = [9, 5, 1, 4, 3]
print(f"Original List: {original_list}")
insertion_sort_with_trace(original_list.copy())