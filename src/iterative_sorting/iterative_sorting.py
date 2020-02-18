# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # TO-DO: swap

        curr_arr = arr[smallest_index:]
        min_val = min(curr_arr)
        idx_min_val = curr_arr.index(min_val)
        cur_index_val = arr[i]

        if (idx_min_val):
            arr.insert(smallest_index, min_val)  # swap value in the main arr
            arr.pop(smallest_index + 1)

            # swap value in the current arr
            curr_arr.insert(idx_min_val, cur_index_val)
            curr_arr.pop(idx_min_val + 1)

            # del all values from the smallest index
            del arr[smallest_index + 1:]

            arr = arr + curr_arr[1:]  # concat new arr with current arr

    print(arr)
    return arr


selection_sort([1, 2, 3, 4, 1, 1, 1, 4, 5])

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
