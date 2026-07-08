import random
import time
import tracemalloc
import csv
import sys

import os
print("Current folder:", os.getcwd())

#increased recursion limit because Quick Sort can go deep
# when the data is already sorted or reverse sorted
sys.setrecursionlimit(100000)

# Merge Sort
# Keep dividing the lists into smaller parts until each part has one or zero elements.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Find the middle index so we can split the list into two halves.
    middle = len(arr) // 2
    
    # Recursively sort the left and right halves
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    
    # Merge the two sorted halves together
    return merge(left_half, right_half)

# This helper function combines two sorted lists into one sorted list
def merge(left, right):
    result = []
    i = 0
    j = 0
    
    # Compare values from both lists and add the smaller one first
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Add any values that are still left over
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Quick Sort
# This funcction picks a pivot and separates values around it.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Last value are used as pivot for this implementation.
    # It makes it easy to see why sorted data can be bad for Quick Sort.
    pivot = arr[-1]
    
    left = []
    equal = []
    right = []
    
    # Put smaller values on the left, bigger values on the right, and same values in the equal list.
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            equal.append(value)
            
    # Recursively sort the left and right parts, then combine everything
    return quick_sort(left) + equal + quick_sort(right)

# This function measures how long the sorting takes and how much memory is used while sorting.
def measure_performance(sort_function, data):
    tracemalloc.start()
    
    start_time = time.perf_counter()
    sorted_data = sort_function(data.copy())
    end_time = time.perf_counter()
    
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    peak_memory_kb = peak_memory / 1024
    
    return execution_time, peak_memory_kb
            
# Creates the datasets that will be used for testing
def create_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))
    random_data = random.sample(range(size * 2), size)
    
    return {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_sorted_data,
        "Random": random_data 
    }
    
# Runs all tests and saves the result in a CSV file.
def run_tests():
    # Kept the sizes reasonable so the program runs without taking too long.
    sizes = [1000, 3000, 5000]
    
    results = []
    
    print("Algorithm, Dataset, Size, Execution Time (seconds), Peak Memory (KB)")
    
    for size in sizes:
        datasets = create_datasets(size)
        
        for dataset_name, data in datasets.items():
            
            # Test Merge Sort
            merge_time, merge_memory = measure_performance(merge_sort, data)
            merge_result = [
                "Merge Sort",
                dataset_name,
                size,
                round(merge_time, 6),
                round(merge_memory, 2)
            ]
            results.append(merge_result)
            print(",".join(map(str, merge_result)))
            
            # Test Quick Sort
            quick_time, quick_memory = measure_performance(quick_sort, data)
            quick_result = [
                "Quick Sort",
                dataset_name,
                size,
                round(quick_time, 6),
                round(quick_memory, 2)
            ]
            results.append(quick_result)
            print(",".join(map(str,quick_result)))
            
    # Save results to a CSV file so it can be used for the report
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow([
            "Algorithm",
            "Dataset",
            "Size",
            "Execution Time (seconds)",
            "Peak Memory (KB)"
        ])
        
        writer.writerows(results)
        
    print("\nResults saved to results.csv")
    
# Main program
if __name__ == "__main__":
    run_tests()
    
            