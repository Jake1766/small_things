# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

# sort values at odd indices of array in non-increasing order
# sort values at even indices of array in non-decreasing order
# non increasing order means that each element is no larger than any
# previous elements

nums1 = [4, 1, 2, 3]

def sort(arr):
    odds = []
    evens = []

    for ind in range(len(arr)):
        if ind % 2 == 0:
            evens.append(arr[ind])
        else:
            odds.append(arr[ind])

    odds = sorted(odds, reverse=True)
    evens = sorted(evens)

    print(odds)
    print(evens)

    for i in range(len(arr)):


sort(nums1)
