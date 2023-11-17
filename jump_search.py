import time

def jump_search(arr, target):
    start_time = time.time()
    n = len(arr)
    step = int(n ** 0.5)
    prev, current = 0, 0

    while current < n and arr[current] < target:
        prev = current
        current += step

    for i in range(prev, min(current, n)):
        if arr[i] == target:
            elapsed_time = (time.time() - start_time) * 1000
            return i

    return -1

'''def jump_search
numbers = list(range(1, 10001))
test_data = ", ".join(map(str, numbers))
target = 9877
array = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("jump_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
result = jump_search(array, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")  '''