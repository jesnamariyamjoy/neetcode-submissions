import math


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        max_div_10 = INT_MAX // 10
        min_div_10 = int(INT_MIN / 10)  # -214748364 (truncates toward zero)

        res = 0
        while x != 0:
            # Truncating division toward zero and remainder matching sign of x
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > max_div_10 or (res == max_div_10 and digit > 7):
                return 0
            if res < min_div_10 or (res == min_div_10 and digit < -8):
                return 0

            res = res * 10 + digit

        return res