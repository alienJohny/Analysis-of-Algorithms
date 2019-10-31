def insert_sort(a):
    size = len(a)
    for c in range(1, size):
        tmp = a[c]
        i = c - 1

        while (i >= 0 and a[i] > tmp):
            a[i + 1] = a[i]
            a[i] = tmp
            i -= 1

    return a

