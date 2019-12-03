def longest_con_seq(arr):

    arr = set(arr)
    max_len = 0

    for num in arr:

        if not num - 1 in arr:

            y = num + 1

            while y in arr:
                y += 1

            max_len = max(max_len, y - num)

    return max_len


arr = [100, 4, 200, 1, 201, 5, 199, 3, 2]
ans = longest_con_seq(arr)
print(ans)
