import time

def interpolation_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            elapsed_time = (time.time() - start_time) * 1000
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

''''#def interpolation_search
numbers = list(range(1, 1001))
test_data = ", ".join(map(str, numbers))
target = 29
array = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("interpolation_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
result = interpolation_search(array, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")'''
