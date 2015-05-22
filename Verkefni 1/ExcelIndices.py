def excel_index(s):
    k = 0
    for i, x in enumerate(s[::-1]):
        k += ord(x) - 64 * 26 ** i

    return k



