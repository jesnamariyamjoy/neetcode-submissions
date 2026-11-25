class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # span = right - left; at least 2 so there is at least one balloon k inside (left, right)
        for span in range(2, n + 2):
            for left in range(n + 2 - span):
                right = left + span
                left_val = arr[left]
                right_val = arr[right]
                best = 0
                row_left = dp[left]

                for k in range(left + 1, right):
                    coins = row_left[k] + left_val * arr[k] * right_val + dp[k][right]
                    if coins > best:
                        best = coins

                row_left[right] = best

        return dp[0][n + 1]