def two_sum(a, b):
    x = 0
    y = len(a) - 1
    res_list = []
    while x < y:
        if a[x] + a[y] > b:
            y -= 1
        elif a[x] + a[y] < b:
            x += 1
        elif a[x] + a[y] == b:
            res_list.append((x, y))
            x += 1
            y -= 1


print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 18))
