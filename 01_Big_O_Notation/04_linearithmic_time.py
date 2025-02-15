# Linearithmic time O(n log n)

# Merge sort splits the array in half recursively (log n), and then merges the halves in linear time (n). Thus, the overall time complexity is O(n log n).

def merge_sort(arr):
    # Merge Sort is an O(n log n) algorithm
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sort the first half
        merge_sort(right_half)  # Sort the second half

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Test the merge_sort function
arr = [12, 11, 13, 5, 6, 7]
result = merge_sort(arr)
print(f"Linearithmic Time Example: {result}")
