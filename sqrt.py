import math

def sqrt_binary_search(number):
    if number < 0:
        return "Invalid number"

    if number == 0 or number == 1:
        return "{:.2f}".format(number)

    # use binary search here
    low = 0
    high = number
    while high - low > 0.000001: # how accurate you want
        mid = (low + high) / 2
        mid_sq = mid * mid

        if mid_sq > number:
            high = mid
        else:
            low = mid

    return "{:.2f}".format(mid)

num = 5
print(sqrt_binary_search(num))
print("{:.2f}".format(math.sqrt(num)))
