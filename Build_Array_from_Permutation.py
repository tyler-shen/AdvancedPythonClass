def buildArray(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

# def buildArray(nums):
#     return [nums[i] for i in nums]

nums = [0,2,1,5,3,4]
print(buildArray(nums))
