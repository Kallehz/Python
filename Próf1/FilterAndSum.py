# Write a function filter_sum(lis) that takes a list of integers as an argument.
# The function returns a pair (2-tuple). The second element of the tuple are the
# elements of the list lis where all the integers smaller than 10 and larger than
# 95 have been removed. The first element of the tuple is the sum of the elements of
# that list.

def filter_sum(lis):
    l = []
    for x in lis:
        if 10 <= x <= 95:
            l.append(x)
    return tuple((sum(lis), l))
    

##def filter_sum(lis):
##    l = []
##    for x in lis:
##        if x >= 10 and x <= 95:
##            l.append(x)
##    return(sum(l), l)

print(filter_sum([1, 9, 30, 12]))
print(filter_sum([88, 1, 119, -12, -10, -18, 117, 26, 46, 37, 9, 63, 9, 125, 18, 111, 6, 8, 34, 116, 75, 21, -7, 94, 32, 61, -28, 10, 61, 86],))

