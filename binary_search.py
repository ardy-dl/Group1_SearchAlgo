import time
import timeit

def binary_search(array, target, low, high):
    low, high = 0, len(array) - 1
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            elapsed_time = (time.time() - start_time) * 1000
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

'''def binary_search
numbers = list(range(1, 10001))
test_data = ", ".join(map(str, numbers))
target = 12
array = list(map(int, test_data.split(",")))
low, high = 0, len(array) - 1
execution_time = timeit.timeit("binary_search(array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
result = binary_search(array, target, low, high)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")'''
