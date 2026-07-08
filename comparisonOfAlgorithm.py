# Merge Sort
# This function keeps dividing the list into smaller parts
# until each part has one or zero elements.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the middle index so we can split the list into two halves
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
# This function picks a pivot and separates values around it.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # I used the last value as the pivot for this implementation
    pivot = arr[-1]

    left = []
    equal = []
    right = []

    # Put smaller values on the left, bigger values on the right,
    # and same values in the equal list
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            equal.append(value)

    # Recursively sort the left and right parts, then combine everything
    return quick_sort(left) + equal + quick_sort(right)