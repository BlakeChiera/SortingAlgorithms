def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
    
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

arr2 = [37, 100, 24, 9, 34, 60, 4, 32, 38, 87, 77, 86, 54, 95, 91, 11, 84, 23, 89, 65]

bubbleSort(arr2)

print(arr2)
print("Sorted array is:")
for i in range(len(arr2)):
    print(arr2[i], end=" ")
