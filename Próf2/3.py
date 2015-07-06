# Numbers game
#
# Hawk and his little brother, Stone, are playing a little game with
#     the following rules. Initially 8 random integers, from 1 to 100 (inclusive),
#     are laid on the table for both players to see. The players then have
#     2 minutes to construct a sequence of numbers, from the given 8 numbers, with the following conditions.
#
# The sum of two adjacent numbers cannot be divisible by 3.
# Immediately to the right of each even number must
# be an odd number or an even number that starts with the digit 1.
# Immediately to the right of each odd number must be either a larger
# even number or an odd number that ends with the digit 5.
# The player who constructs the longer sequence wins.
# Just before the two minutes are up, Stone notices that he
# can construct a legal sequence using all 8 numbers. However, in all the excitement,
# he knocks all the numbers off the table, and cannot remember how to construct the sequence.
# Hawk is very sceptical of his brother, so he asks you to write a program that determines whether
# his brother is telling the truth or not.
#
# Write a function numbers_game that takes a list of 8 integers
# (in the range from 1 to 100) as input. The function returns
# True if it is possible to construct a legal sequence from the 8 integers;
# False otherwise.

from itertools import permutations
def numbers_game(lis):
    for perm in permutations(lis):
        valid = True
        for i in range(0, len(lis)-1):
            # The sum of two adjacent numbers cannot be divisible by 3.
            if not ((perm[i] + perm[i+1]) % 3 != 0):
                valid = False
            # Immediately to the right of each even number must be an odd number or an even number that starts with the digit 1.
            if perm[i] % 2 == 0:
                if not((perm[i+1] % 2 != 0) or (perm[i+1] % 2 == 0 and str(perm[i+1]).startswith('1'))):
                    valid = False
            # Immediately to the right of each odd number must be either a larger even number or an odd number that ends with the digit 5.
            if perm[i] % 2 != 0:
                if not((perm[i+1] % 2 == 0 and perm[i+1] > perm[i]) or (perm[i+1] % 2 != 0 and str(perm[i+1]).endswith('5'))):
                    valid = False


        if valid:
            return True
    return valid
#
print(numbers_game([68, 45, 19, 54, 56, 51, 94, 7]))
# # True
print(numbers_game([3, 2, 4, 6, 3, 3, 15, 3]))
# # False
print(numbers_game([61, 50, 35, 53, 5, 45, 41, 6]))
# True