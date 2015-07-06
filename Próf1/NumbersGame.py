# Hawk and his little brother, Stone, are playing a little game with
# the following rules. Initially 8 random integers, from 1 to 100
# (inclusive), are laid on the table for both players to see. The
# players then have 2 minutes to construct a sequence of numbers, from
# the given 8 numbers, with the following conditions. To the right
# of each even number must be either be an odd number, or the same even
# number. To the right of each odd number must be either a larger even
# number or a strictly smaller odd number. The player who constructs the
# longer sequence wins. Just before the two minutes are up, Stone
# notices that he can construct a legal sequence using all 8 numbers.
# However, in all the excitement, he knocks all the numbers off the
# table, and cannot remember how to construct the sequence. Hawk is very
# sceptical of his brother, so he asks you to write a program that
# determines whether his brother is telling the truth or not.
# Write a function numbers_game that takes a list of 8 integers (in the range
# from 1 to 100) as input. The function returns True if it is possible
# to construct a legal sequence from the 8 integers; False otherwise.


from itertools import permutations
def numbers_game(lis):
    for perm in permutations(lis):
        valid = True
        for i in range(0, len(lis)-1):
            #To the right of each even number must be either be an odd number, or the same evennumber.
            if perm[i] % 2 == 0:
                if not(perm[i+1] % 2 != 0 or perm[i] == perm[i+1]):
                    valid = False
                    break
            #To the right of each odd number must be either a larger even number or a strictly smaller odd number.
            if perm[i] % 2 != 0:
                if not((perm[i+1] > perm[i] and perm[i+1] % 2 == 0) or (perm[i+1] < perm[i] and perm[i+1] % 2 != 0)):
                    valid = False
                    break

        if valid:
            return True
    return valid


##def numbers_game(lis):
##    for perm in permutations(lis):
##        if isValid(perm):
##            return True
##    return False
##
##def isValid(perm):
##    for i in range(0, len(perm)-1):
##        # To the right of each even number must be either be an odd number, or the same even number.
##        if perm[i] % 2 == 0:
##            if (perm[i+1] % 2 != 0 or perm[i] == perm[i+1]):
##                continue
##            else:  
##                return False
##        # To the right of each odd number must be either a larger even number or a strictly smaller odd number.
##        if perm[i] % 2 != 0:
##            if (perm[i+1] > perm[i] and perm[i+1] % 2 == 0) or (perm[i+1] < perm[i] and perm[i+1] % 2 != 0):
##                continue
##            else:
##                return False
##            
##    return True
 
print(numbers_game([8,3,29,12,7,1,20,39]))
#True
print(numbers_game([3,2,4,6,3,3,15,3]))
#False
