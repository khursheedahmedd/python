def partition(nums, low, high):
    pivot = nums[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1  # Increment the index of the smaller element
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements

    # Swap the pivot element with the element at i+1
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1  # Return the partitioning index

def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)  # Partition the array

        quick_sort(nums, low, pi - 1)  # Recursively sort the left part
        quick_sort(nums, pi + 1, high)  # Recursively sort the right part

# Example usage
nums = [3, 1, 6, 3, 18, 10, 5]
n = len(nums)

quick_sort(nums, 0, n - 1)  # Sorting the entire list
print(nums)  # Output the sorted list
