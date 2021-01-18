"""
It divides the input array into two halves, calls itself for the two halves,
and then merges the two sorted halves. The merge() function is used for merging
two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r]
are sorted and merges the two sorted sub-arrays into one.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

"""

def merge_sort(arr):
    mid = len(arr)//2
    left_array=arr[0:mid]
    right_array=arr[mid:]
    merge_sort(left_array)
    merge_sort(right_array)

    i=j=k=0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k]=left_array[i]
            i += 1
        else:
            arr[k]=right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        arr[k]=left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1

    return arr

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("original array: " + str(arr))
    arr2=merge_sort(arr)
    print("sorted array: " + str(arr2))
