"""
Bubble sort algorithm travels through the entire sequence of and compares the elements i to i+1. 
It flips the position x[i+1] -> x[i] if x[i] > x[i+1]. It repeats this entire process until the entire
sequence is sorted. The space complexity of this algorithm is O(n^2) ~ n^2/2 + n/2
"""

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == "__main__":
    arr = [10, 2, 18, 4, 31, 13, 5, 23, 51, 29, 64]
    sorted_array = bubble_sort(arr)
    print("Original Array: " + str(arr))
    print("Sorted Array: " + str(sorted_array))


   
