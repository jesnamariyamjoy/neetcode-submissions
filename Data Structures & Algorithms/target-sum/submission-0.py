class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total or (total + target) % 2 != 0:
            return 0

        pos_sum = (total + target) // 2
        dp = [0] * (pos_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(pos_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[pos_sum]