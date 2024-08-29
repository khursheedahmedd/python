def conquer(nums, si, mid, ei):
    merged = []
    idx1 = si  # Start index of the first half
    idx2 = mid + 1  # Start index of the second half

    while idx1 <= mid and idx2 <= ei:
        if nums[idx1] <= nums[idx2]:
            merged.append(nums[idx1])
            idx1 += 1
        else:
            merged.append(nums[idx2])
            idx2 += 1

    # Copy remaining elements of the first half
    while idx1 <= mid:
        merged.append(nums[idx1])
        idx1 += 1

    # Copy remaining elements of the second half
    while idx2 <= ei:
        merged.append(nums[idx2])
        idx2 += 1

    # Copy sorted elements back into original array
    for i in range(len(merged)):
        nums[si + i] = merged[i]

def divide(nums, si, ei):
    if si >= ei:  # Base case: single element or invalid range
        return
    
    mid = si + (ei - si) // 2  
    divide(nums, si, mid)      
    divide(nums, mid + 1, ei)  
    conquer(nums, si, mid, ei)

# Example usage
nums = [3, 1, 6, 3, 18, 10, 5]
n = len(nums)

divide(nums, 0, n - 1)  # Sorting the entire list
print(nums)  # Output the sorted list
