import itertools
def numbers_game(lis):
    return list(itertools.permutations(lis))
    











print(numbers_game([8,3,29,12,7,1,20,39]))
True
print(numbers_game([3,2,4,6,3,3,15,3]))
False
