def bubble_sort_with_trace(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Pass {i+1}: {arr}")
        if not swapped:
            break
    return arr

# Test the function
original_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original List: {original_list}")
bubble_sort_with_trace(original_list.copy())