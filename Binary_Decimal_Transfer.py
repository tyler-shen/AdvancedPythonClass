# Decimal to Binary
def getBits(num):
    result = ""
    while num > 0:
        bit = num % 2
        num //= 2
        result = str(bit) + result
    while len(result) % 4 != 0 or len(result) == 0:
        result = "0" + result
    return result

# Binary to Decimal
def getNums(bit):
    result = 0
    length = len(bit)
    for char in bit:
        length -= 1
        if char == "1":
            result += pow(2, length)
    return result

# Decimal XOR
# num1 ^ num2
# Binary XOR
def getXorByBits(bits1, bits2):
    max_len = max(len(bits1), len(bits2))
    while len(bits1) < max_len:
        bits1 = "0" + bits1
    while len(bits2) < max_len:
        bits2 = "0" + bits2

    resultBits = ""
    for i in range(max_len):
        if bits1[i] == bits2[i]:
            resultBits += "0"
        else:
            resultBits += "1"
    return resultBits
