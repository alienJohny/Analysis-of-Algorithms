def quick_sort(a):
    "User-friendly wrapper"

    def qs_subroutine(a, left, right):
        i = left
        j = right
        pivot = a[(left + right) // 2]

        while (i <= j):
            while (a[i] < pivot):
                i += 1

            while (a[j] > pivot):
                j -= 1

            if (i <= j):
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        if (left < j):
            qs_subroutine(a, left, j)

        if (i < right):
            qs_subroutine(a, i, right)

    qs_subroutine(a, 0, len(a) - 1)

    return a
