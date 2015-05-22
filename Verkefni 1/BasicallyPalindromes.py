def palindrome(n, b):
    l = []
    while n != 0:
        r = n % b
        n = n // b
        l += [r]
    return l == l[::-1]
