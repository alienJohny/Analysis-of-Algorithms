def bm_search(haystack, needle):
    """
    Search list `haystack` for sub-list `needle`.
    """
    if len(needle) == 0:
        return 0
    char_table = make_char_table(needle)
    offset_table = make_offset_table(needle)
    i = len(needle) - 1
    while i < len(haystack):
        j = len(needle) - 1
        while needle[j] == haystack[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(offset_table[len(needle) - 1 - j], char_table.get(haystack[i]));
    return -1


def make_char_table(needle):
    """
    Makes the jump table based on the mismatched character information.
    """
    table = {}
    for i in range(len(needle) - 1):
        table[needle[i]] = len(needle) - 1 - i
    return table


def make_offset_table(needle):
    """
    Makes the jump table based on the scan offset in which mismatch occurs.
    """
    table = []
    last_prefix_position = len(needle)
    for i in reversed(range(len(needle))):
        if is_prefix(needle, i + 1):
            last_prefix_position = i + 1
        table.append(last_prefix_position - i + len(needle) - 1)
    for i in range(len(needle) - 1):
        slen = suffix_length(needle, i)
        table[slen] = len(needle) - 1 - i + slen
    return table


def is_prefix(needle, p):
    """
    Is needle[p:end] a prefix of needle?
    """
    j = 0
    for i in range(p, len(needle)):
        if needle[i] != needle[j]:
            return 0
        j += 1   
    return 1


def suffix_length(needle, p):
    """
    Returns the maximum length of the substring ending at p that is a suffix.
    """
    length = 0;
    j = len(needle) - 1
    for i in reversed(range(p + 1)):
        if needle[i] == needle[j]:
            length += 1
        else:
            break
        j -= 1
    return length

def test():    
    tests = [
        ["000110", "01", 2],
        ["abcdef", "de", 3],
        ["acgtagtcgtc", "gtcg", 5],
        ["atgcatcg", "gta", -1]]

    for t in tests:
        status = None
        haystack = t[0]
        needle = t[1]
        ground_true = t[2]

        response = bm_search(haystack, needle)

        if response == ground_true:
            status = "OK"
        else:
            status = "ERROR"

        print("Tested haystack '{0}' and needle '{1}', ground true: {2}, found: {3}. {4}".format(
            haystack, needle, ground_true, response, status))


def main():
    test()

if __name__ == "__main__":
    main()
