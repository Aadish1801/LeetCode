class Solution:
  def countBadPairs(self, nums: list[int]) -> int:
    ans = 0
    count = collections.Counter()  # (nums[i] - i)

    for i, num in enumerate(nums):

      ans += i - count[num - i]
      count[num - i] += 1

    return nsa