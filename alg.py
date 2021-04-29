def bitonic_merge_sort(collection):

    def sort_phase(ascending: bool, collection: list):

        collection_size = len(collection)

        if collection_size <= 1:
            return collection
        else:
            first_slice = sort_phase(True, collection[:collection_size // 2])
            second_slice = sort_phase(False, collection[collection_size // 2:])
            return merge_phase(ascending,  first_slice + second_slice)

    def merge_phase(ascending: bool, collection):

        if len(collection) == 1:
            return collection
        else:
            compare_n_swap(ascending, collection)
            first = merge_phase(ascending, collection[:len(collection) // 2])
            second = merge_phase(ascending, collection[len(collection) // 2:])
            return first + second

    def compare_n_swap(ascending: bool, collection):

        distance = len(collection) // 2
        for i in range(distance):
            if (collection[i] > collection[i + distance]) == ascending:
                collection[i], collection[i +distance] = collection[i + distance], collection[i]

    return sort_phase(True, collection)
