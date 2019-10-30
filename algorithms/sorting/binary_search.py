def binary_search(array, val):

    lo, hi = 0, len(array) - 1

    while (lo <= hi):

        mid = lo + (hi - lo) // 2

        if array[mid] == val:
            return mid

        if array[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1

    breakpoint()
    if array[mid] < val or mid == 0:
        return array[mid]
    else:
        return array[mid-1]


def binary_search_recursive(array, val, lo, hi):

    if lo > hi:
        return None

    mid = (hi - lo)//2 + lo

    if array[mid] == val:
        return mid
    elif array[mid] > val:
        return binary_search_recursive(array, val, lo, mid - 1)
    else:
        return binary_search_recursive(array, val, mid + 1, hi)


array = [100, 150, 180, 220]
ans = binary_search(array, 170)
print(ans)
