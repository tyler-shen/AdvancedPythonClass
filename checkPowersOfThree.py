def checkPowersOfThree(n):
    # base case
    if n == 0:
        return True

    # regular case
    if n % 3 == 2:
        return False
    else:
        return checkPowersOfThree(n // 3)


n = 12
print(checkPowersOfThree(n))
