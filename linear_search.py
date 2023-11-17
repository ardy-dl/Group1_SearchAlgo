import time

def linear_search(arr, target):
    start_time = time.time()

    for i in range(len(arr)):
        if arr[i] == target:
            elapsed_time = (time.time() - start_time) * 1000
            return i

    return -1

'''#def linear_search
numbers = list(range(1, 1001))
test_data = ", ".join(map(str, numbers))
target = 29
array = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("linear_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
result = linear_search(array, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {result} ")'''