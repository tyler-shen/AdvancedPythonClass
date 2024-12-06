
# O(n^2)
def maximumDifference(self, nums: List[int]) -> int:
    diff = -1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                diff = max(diff, nums[j] - nums[i])
    return diff


# O(n)
  def maximumDifference(self, nums: List[int]) -> int:
      num1 = nums[0]
      diff = -1
      for num2 in nums:
          if num2 > num1:
              diff = max(diff, num2 - num1)
          else: # even if there is a large number later, the difference between the large number and num2 would be definitely greater than num1
              num1 = num2
      return diff
