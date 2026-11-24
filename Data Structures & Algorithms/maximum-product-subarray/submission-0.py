from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for x in nums[1:]:
            temp_max = max(x, cur_max * x, cur_min * x)
            cur_min = min(x, cur_max * x, cur_min * x)
            cur_max = temp_max
            res = max(res, cur_max)

        return res