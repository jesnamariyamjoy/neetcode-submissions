class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            max_sum = max(max_sum, cur_sum)

        return max_sum