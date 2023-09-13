# Define the array
arr = [-5, 9, 33, 67, -22, 17, 3]

# Selection Sort Algorithm
for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    # Swap the found minimum element with the current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Print the sorted array
print(arr)
