# # approach 1
# # time limit problem if k is way too large
# def getWinner(arr, k):
#     count = 0
#     while True:
#         if arr[0] > arr[1]:
#             arr.append(arr.pop(1))
#             count += 1
#         else:
#             arr.append(arr.pop(0))
#             count = 1
#         if count == k:
#             return arr[0]


# # approach 2
# # works but can be better
# def getWinner(arr, k):
#     size = len(arr)
#     count = 0
#     if k >= size:
#         return max(arr)

#     while True:
#         if arr[0] > arr[1]:
#             arr.append(arr.pop(1))
#             count += 1
#         else:
#             arr.append(arr.pop(0))
#             count = 1
#         if count == k:
#             return arr[0]


# approach 3
# only go through arr once
def getWinner(arr, k):
    size = len(arr)
    count = 0
    max_num = max(arr)
    result = arr[0]
    if k >= size:
        return max_num

    for i in range(1, size):
        if result > arr[i]:
            count += 1
        else:
            result = arr[i]
            count = 1

        if count == k:
            return result

    return result


# arr = [2,1,3,5,4,6,7]
# k = 2
# arr = [3,2,1]
# k = 10
arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000
