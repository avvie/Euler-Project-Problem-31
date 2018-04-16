# import sys
# sys.setrecursionlimit(10000)


Coins = [1,2,5,10,20,50,100,200]

def FindCombCoun(amount, index):
    if amount is 0:
        return 1
    elif amount < 0 or index >= len(Coins):
        return 0
    else:
        return FindCombCoun(amount - Coins[index], index) + FindCombCoun(amount, index + 1)

print(str(FindCombCoun(200, 0)))