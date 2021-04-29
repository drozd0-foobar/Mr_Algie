import alg
import random

# Adjust spread values here
spreads_from = 0
spreads_to = 1000000

arr_16 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 4))]
arr_256 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 8))]
arr_1024 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 10))]
arr_32_768 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 15))]
arr_524_288 = [random.randint(spreads_from, spreads_to) for i in range(pow(2, 19))]

# Adjust arr value here
arr = arr_32_768

print("LIST: ", arr)
sorted_arr = alg.bitonic_merge_sort(arr)
print("SORTED LIST:", sorted_arr)
