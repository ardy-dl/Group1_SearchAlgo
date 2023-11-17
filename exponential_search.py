import time
from binary_search import binary_search

def exponential_search(arr, target):
    start_time = time.time()

    if arr[0] == target:
        return 0

    i = 1
    n = len(arr)

    while i < n and arr[i] <= target:
        i *= 2

    result, _ = binary_search(arr, target, 0, min(i, n) - 1)
    elapsed_time = (time.time() - start_time) * 1000

    return result

'''#def exponential_search
numbers = list(range(1, 1001))
test_data = ", ".join(map(str, numbers))
target = 29
array = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("exponential_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
result = exponential_search(array, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")'''