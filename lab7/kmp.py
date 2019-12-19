def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

def kmp(s, t):
    index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k - 1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index

def test():
    tests = [
        ["000110", "01", 2],
        ["abcdef", "de", 3],
        ["acgtagtcgtc", "gtcg", 5],
        ["atgcatcg", "gta", -1],
        ["abababcb", "ababcb", 2]]

    for t in tests:
        status = None
        haystack = t[0]
        needle = t[1]
        ground_true = t[2]

        response = kmp(needle, haystack)

        if response == ground_true:
            status = "OK"
        else:
            status = "ERROR"

        print("Tested haystack '{0}' and needle '{1}', ground true: {2}, found: {3}. {4}".format(
            haystack, needle, ground_true, response, status))

test()
