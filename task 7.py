import time
import sys

# All sorting algorithms with counters for comparisons and swaps

def bubble_sort_with_stats(arr):
    """Bubble Sort with comparison and swap counters"""
    comparisons = 0
    swaps = 0
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

def insertion_sort_with_stats(arr):
    """Insertion Sort with comparison and swap counters"""
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        
        arr[j + 1] = key
    return arr, comparisons, swaps

def quick_sort_with_stats(arr):
    """Quick Sort with comparison and swap counters"""
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    
    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1
    
    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)
    
    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps

def merge_sort_with_stats(arr):
    """Merge Sort with comparison and swap counters"""
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    
    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            swaps += 1
        
        while i < len(left):
            result.append(left[i])
            swaps += 1
            i += 1
        
        while j < len(right):
            result.append(right[j])
            swaps += 1
            j += 1
        
        return result
    
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        return merge(left, right)
    
    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, swaps

# Function to measure memory usage (basic observation)
def get_memory_usage():
    """Basic memory observation - returns approximate memory in bytes"""
    return sys.getsizeof([])  # Base memory for reference

# Main comparison function
def compare_sorting_algorithms(dataset):
    """Compare all sorting algorithms with the given dataset"""
    
    print("=" * 80)
    print("SORTING ALGORITHMS COMPARISON")
    print("=" * 80)
    print(f"\nDataset: {dataset}")
    print(f"Dataset Size: {len(dataset)} elements\n")
    
    results = []
    
    # Test Bubble Sort
    print("Testing Bubble Sort...")
    arr_copy = dataset.copy()
    start_time = time.time()
    sorted_arr, comparisons, swaps = bubble_sort_with_stats(arr_copy)
    end_time = time.time()
    time_taken = end_time - start_time
    memory_usage = "O(1) - In-place"
    results.append(["Bubble Sort", comparisons, swaps, time_taken, memory_usage])
    print(f"  ✓ Completed in {time_taken:.6f} seconds")
    
    # Test Insertion Sort
    print("Testing Insertion Sort...")
    arr_copy = dataset.copy()
    start_time = time.time()
    sorted_arr, comparisons, swaps = insertion_sort_with_stats(arr_copy)
    end_time = time.time()
    time_taken = end_time - start_time
    memory_usage = "O(1) - In-place"
    results.append(["Insertion Sort", comparisons, swaps, time_taken, memory_usage])
    print(f"  ✓ Completed in {time_taken:.6f} seconds")
    
    # Test Quick Sort
    print("Testing Quick Sort...")
    arr_copy = dataset.copy()
    start_time = time.time()
    sorted_arr, comparisons, swaps = quick_sort_with_stats(arr_copy)
    end_time = time.time()
    time_taken = end_time - start_time
    memory_usage = "O(log n) - In-place"
    results.append(["Quick Sort", comparisons, swaps, time_taken, memory_usage])
    print(f"  ✓ Completed in {time_taken:.6f} seconds")
    
    # Test Merge Sort
    print("Testing Merge Sort...")
    arr_copy = dataset.copy()
    start_time = time.time()
    sorted_arr, comparisons, swaps = merge_sort_with_stats(arr_copy)
    end_time = time.time()
    time_taken = end_time - start_time
    memory_usage = "O(n) - Additional array"
    results.append(["Merge Sort", comparisons, swaps, time_taken, memory_usage])
    print(f"  ✓ Completed in {time_taken:.6f} seconds")
    
    # Display comparison table
    print("\n" + "=" * 80)
    print("COMPARISON TABLE")
    print("=" * 80)
    
    # Table header
    print(f"{'Algorithm':<15} {'Comparisons':<12} {'Swaps':<10} {'Time Taken':<15} {'Memory Usage':<20}")
    print("-" * 80)
    
    # Table rows
    for result in results:
        print(f"{result[0]:<15} {result[1]:<12} {result[2]:<10} {result[3]:<15.6f} {result[4]:<20}")
    
    print("=" * 80)
    
    # Find fastest algorithm
    fastest = min(results, key=lambda x: x[3])
    print(f"\n✓ Fastest Algorithm: {fastest[0]} ({fastest[3]:.6f} seconds)")
    
    # Find algorithm with fewest comparisons
    min_comparisons = min(results, key=lambda x: x[1])
    print(f"✓ Fewest Comparisons: {min_comparisons[0]} ({min_comparisons[1]} comparisons)")
    
    # Find algorithm with fewest swaps
    min_swaps = min(results, key=lambda x: x[2])
    print(f"✓ Fewest Swaps: {min_swaps[0]} ({min_swaps[2]} swaps)")
    
    return results

# Test with different datasets

# Dataset 1: Random data (same as example)
print("\n" + "=" * 80)
print("TEST 1: STANDARD DATASET")
print("=" * 80)
dataset1 = [64, 34, 25, 12, 22, 11, 90]
compare_sorting_algorithms(dataset1)

# Dataset 2: Larger random dataset
print("\n" + "=" * 80)
print("TEST 2: LARGER DATASET")
print("=" * 80)
dataset2 = [64, 34, 25, 12, 22, 11, 90, 5, 3, 42, 18, 29, 7, 15, 88, 45]
compare_sorting_algorithms(dataset2)

# Dataset 3: Nearly sorted data
print("\n" + "=" * 80)
print("TEST 3: NEARLY SORTED DATASET")
print("=" * 80)
dataset3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
compare_sorting_algorithms(dataset3)

# Dataset 4: Reverse sorted data (worst case)
print("\n" + "=" * 80)
print("TEST 4: REVERSE SORTED DATASET (WORST CASE)")
print("=" * 80)
dataset4 = [90, 82, 64, 43, 38, 34, 27, 25, 22, 12, 11, 10, 9, 5, 3]
compare_sorting_algorithms(dataset4)