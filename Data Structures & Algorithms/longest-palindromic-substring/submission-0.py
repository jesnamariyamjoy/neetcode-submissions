class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_len = 0

        def expand(left: int, right: int) -> None:
            nonlocal best_start, best_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > best_len:
                    best_start = left
                    best_len = curr_len
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd length
            expand(i, i)
            # Even length
            expand(i, i + 1)

        return s[best_start : best_start + best_len]