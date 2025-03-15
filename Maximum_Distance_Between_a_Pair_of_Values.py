def maxDistance_basic(nums1, nums2):
    result = 0
    for i in range(len(nums1)):
        for j in range(i, len(nums2)):
            if nums1[i] <= nums2[j]:
                result = max(result, j - i)
    return result

def maxDistance_adv(nums1, nums2):
    result = 0
    for i in range(len(nums1)):
        left = i
        right = len(nums2) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums1[i] <= nums2[mid]:
                result = max(result, mid - i)
                left = mid + 1
            else:
                right = mid - 1

        if len(nums2) - i < result:
            break

    return result


nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]
print(maxDistance_adv(nums1, nums2))
