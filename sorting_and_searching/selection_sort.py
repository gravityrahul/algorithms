"""
Selection sort keeping track of the minimum value and swapping two elements of the list.
The space complexity is O(n^2)
"""
def selection_sort(array):
    #i indicates the number of items have been sorted.
    n = len(array)
    for i in range(n-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index=i
        # We then use j to loop through the remaining elements
        for j in range(i+1, n-1):
            if array[j] < array[min_index]:
                min_index =j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    arr = [3, 1, 41, 59, 26, 53, 59]
    sorted_array = selection_sort(arr)
    print("Original Array: " + str(arr))
    print("Sorted Array: " + str(sorted_array))

