import random
from alg import bitonic_merge_sort

# Adjust spread values here
spreads_from = 0
spreads_to = 1000000
#
arr_16 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 4))]
arr_256 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 8))]
arr_1024 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 10))]
arr_32_768 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 15))]
arr_524_288 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 19))]
arr_not = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Adjust arr value here
arr = arr_32_768
#
py_sorted = sorted(arr)
print("Testing...")
bitonicmerge_sorted = bitonic_merge_sort(arr)

if py_sorted == bitonicmerge_sorted:
    print(f"{bitonic_merge_sort.__name__} passed the test.")
else: print(f"{bitonic_merge_sort.__name__} did not passed the test")

