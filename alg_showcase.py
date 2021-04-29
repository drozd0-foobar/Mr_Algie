import random


def bitonic_merge_sort(collection):

    def sort_phase(ascending: bool, collection: list):
        print("SORTING... ->", collection)

        collection_size = len(collection)

        if collection_size <= 1:
            print("SORT FINISHED -> (END OF RECURSION):", collection)
            return collection
        else:
            first_slice = sort_phase(True, collection[:collection_size // 2])
            second_slice = sort_phase(False, collection[collection_size // 2:])
            print("SORT PASSED: ", first_slice + second_slice)
            return merge_phase(ascending,  first_slice + second_slice)

    def merge_phase(ascending: bool, collection):
        print("MERGING... ->", collection)

        if len(collection) == 1:
            print("MERGE FINISHED -> (END OF RECURSION): ", collection)
            return collection
        else:
            compare_n_swap(ascending, collection)
            first = merge_phase(ascending, collection[:len(collection) // 2])
            second = merge_phase(ascending, collection[len(collection) // 2:])
            print("MERGE FINISHED: ", first + second)
            return first + second

    def compare_n_swap(ascending: bool, collection):
        print("COMPARING... -> ", collection)

        distance = len(collection) // 2
        for i in range(distance):
            print(f"COMPARING:({i} with {i+distance})...")
            if (collection[i] > collection[i + distance]) == ascending:
                collection[i], collection[i +
                                          distance] = collection[i + distance], collection[i]
                print(f"SWAPPED({i} with {i+distance}): ", collection)
            print("COMPARED.")
    return sort_phase(True, collection)


arr = [random.randint(0, 10) for i in range(pow(2, 3))]
print(arr)
sorted_arr = bitonic_merge_sort(arr)
print(sorted_arr)
