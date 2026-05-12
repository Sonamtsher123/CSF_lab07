def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
original_list = [10, 7, 8, 9, 1, 5]
print(f"Original List: {original_list}")
sorted_list = quick_sort(original_list.copy())
print(f"Sorted List: {sorted_list}")