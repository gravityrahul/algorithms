"""
The implementation of the binary search is done using two approaches:
	a) Recursive: The binary search function is applied recursively to 
                      the low and high values. Where the loe or high values 
                      are decided based on the target value. 
                      if x < mid: low=low, high = mid -1
                      if x > mid: low = mid + 1, high = high

	b) Iterative: The target value is iteratively searched using the array
                      by dividing the array using the same logic above
"""
def binary_search_recursive(array, low, high, x):
    if high >= low: # Always makes sure high is greater than low
        middle = (low+high)//2
        if array[middle]==x:
            return middle
        elif x < array[middle]: # x lies in the left of the array
            return binary_search_recursive(array, low, middle-1, x)
        else:
            return binary_search_recursive(array, middle+1, high, x)

    else:
        return -1


def binary_search_iterative(array, x):
    low = 0
    high = len(array)-1
    while low <= high:
        middle = (low + high)//2
        if x < array[middle]:
            high = middle-1
        elif x > array[middle]:
            low = middle +1
        else:
            return middle

    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 13, 14, 15, 18, 19, 22, 25, 45] 
    x = 10
    indx = binary_search_recursive(arr, 0, len(arr)-1, x)
    print(indx)

    indx2=binary_search_iterative(arr, x)
    print(indx2)
