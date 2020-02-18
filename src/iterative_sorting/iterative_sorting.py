# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # idx_min_val = arr.index(min(arr[smallest_index:]))
        # min_val = min(arr[smallest_index:])
        # cur_index_val = arr[i]
        # min_val_count = arr.count(min_val)
        # # TO-DO: swap
        # if (idx_min_val >= smallest_index):
        #     arr.insert(smallest_index, min_val)
        #     arr.pop(smallest_index + 1)
        #     arr.insert(idx_min_val, cur_index_val)
        #     arr.pop(idx_min_val + 1)
        #     i += 1

        # Find the smallest card. Swap it with the first card.
        # min_val = min(arr)
        curr_arr = arr[smallest_index:]
        # new_arr =
        min_val = min(curr_arr)
        idx_min_val = curr_arr.index(min_val)
        cur_index_val = arr[i]
        print(cur_index, " curr idx")
        print(smallest_index, " sma idx")
        print(curr_arr, "cur arr outof loop")
        print(min_val, " min val outof loop")
        print(cur_index_val, " val of lowe idx")
        print(idx_min_val, "idx of min val")
        print("----------------------")

        # # arr[smallest_index] = min_val
        # print(curr_arr, "cur arr before")
        # # curr_arr.remove(min_val)
        # curr_arr[cur_index] = min_val
        # curr_arr[idx_min_val] = cur_index_val
        # print(curr_arr, "cur arr after rmv")
        # print(arr, " main arr before")
        # # arr.remove(min_val)
        # # arr.pop(idx_min_val + 1)
        # arr = curr_arr
        # print(arr, " main arr after rmv")
        # print("\n")

        # if (idx_min_val >= smallest_index):
        if (idx_min_val):
            print(arr, " main arr before")
            arr.insert(smallest_index, min_val)
            arr.pop(smallest_index + 1)
            curr_arr.insert(idx_min_val, cur_index_val)
            curr_arr.pop(idx_min_val + 1)

            del arr[smallest_index + 1:]

            arr = arr + curr_arr[1:]
            # i += 1
            print(curr_arr, "cur arr after")
            print(arr, " main arr after")
            print("\n")

        # Find the second-smallest card. Swap it with the second card.
        # Find the third-smallest card. Swap it with the third card.
        # Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
    # del arr[2:]
    print(curr_arr)
    print(arr)
    return arr


selection_sort([1, 2, 3, 4, 1, 1, 1, 4, 5])

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
