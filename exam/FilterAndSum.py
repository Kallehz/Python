def filter_sum(lis):
    l = []
    for x in lis:
        if x >= 10 and x <= 95:
            l.append(x)
    return(sum(l), l)

print(filter_sum([1, 9, 30, 12]))
print(filter_sum([88, 1, 119, -12, -10, -18, 117, 26, 46, 37, 9, 63, 9, 125, 18, 111, 6, 8, 34, 116, 75, 21, -7, 94, 32, 61, -28, 10, 61, 86],))

#(42, [30, 12])
