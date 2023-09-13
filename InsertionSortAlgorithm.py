def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Select the current element to be inserted
        j = i - 1  # Start comparing with the previous element

        # Move elements of arr[0..i-1], that are greater than key, one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the greater element to the right
            j -= 1

        arr[j + 1] = key  # Place the current element in its correct position

        # Print the array at this step
        print(f"Step {i}: {arr}")

# Example usage:
arr = [-5, 9, 33, 67, -22, 17, 3]
print("Original Array:", arr)
insertion_sort(arr)
