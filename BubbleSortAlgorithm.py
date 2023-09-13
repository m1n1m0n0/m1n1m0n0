# Define the array
arr = [-5, 9, 33, 67, -22, 17, 3]

# Bubble Sort Algorithm
n = len(arr)
for i in range(n):
    # Flag to optimize the algorithm
    swapped = False
    
    # Last i elements are already in place, so we don't need to check them
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    
    # If no two elements were swapped in the inner loop, the array is already sorted
    if not swapped:
        break

# Print the sorted array
print(arr)
