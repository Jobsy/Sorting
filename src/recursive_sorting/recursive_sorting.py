# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    i = j = 0
    k = []
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            k.append(arrA[i])
            i = i + 1
        else:
            k.append(arrB[j])
            j = j + 1
    # when we exit the loop
    # we are at the end of at least one of the lists
    k.extend(arrA[i:])
    k.extend(arrB[j:])

    # return merged_arr
    return k


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
