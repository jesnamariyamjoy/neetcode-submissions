class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        last_idx = len(nums) - 1

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= last_idx:
                return True

        return True