import timeit
import random
from alg import bitonic_merge_sort

def time_test(arr):
    time = timeit.timeit(f"bitonic_merge_sort({arr})", globals=globals(), number=10)/10
    return f"{time: 7f}s"

print("RANDOM LIST")
for i in range(7, 18):
    arr = [random.randint(0, 1_000_000) for i in range(pow(2, i))]
    print(pow(2, i), time_test(arr))

print("SORTED LIST")
for i in range(7, 18):
    arr = [i for i in range(pow(2, i))]
    print(pow(2, i), time_test(arr))

print("REVERSED LIST")
for i in range(7, 18):
    arr = [ i for i in reversed(range(pow(2, i)))]
    print(pow(2, i), time_test(arr))