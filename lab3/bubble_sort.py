def bubble_sort(a):
    N = len(a)

    for i in range(1, N):
        for j in range(1, N - i + 1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a
