def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

# Приклад використання:
arr = [1.1, 2.2, 3.3, 4.4, 5.5]
target = 3.5
result = binary_search(arr, target)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")
