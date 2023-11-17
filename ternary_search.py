import time

def ternary_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif arr[mid1] < target:
            low = mid1 + 1
        elif arr[mid2] > target:
            high = mid2 - 1
        else:
            low, high = mid1 + 1, mid2 - 1

    return -1

'''def ternary_search
numbers = list(range(1, 1001))
test_data = ", ".join(map(str, numbers))
target = 29
array = list(map(int, test_data.split(",")))
left, right = 0, len(array) - 1
execution_time = timeit.timeit("ternary_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
result = ternary_search(array, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")'''