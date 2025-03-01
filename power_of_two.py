def isPowerOfTwo(n):
    if n == 0:
        return False
    
    if n % 2 == 0:
        return isPowerOfTwo(n // 2)
    else:
        if n == 1:
            return True
        else:
            return False

n = 16
print(isPowerOfTwo(n))
