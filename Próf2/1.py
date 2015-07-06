# Split list
#
# Write a function split(lis) that takes a list of integers as an argument.
# The function returns a pair (2-tuple), both containing a list.
# The first element of the tuple are the elements of lis,
# where negative numbers and odd numbers have been removed.
# The second element of the tuple contains the remaining elements of lis.

def split(lis):
    l = []
    l2 = []
    for x in lis:
        if x < 0 or x % 2 != 0:
            l.append(x)
        else:
            l2.append(x)

    return (l2, l)



print(split([1, 9, 30, -3, 12]))
# ([30, 12], [1, 9, -3])