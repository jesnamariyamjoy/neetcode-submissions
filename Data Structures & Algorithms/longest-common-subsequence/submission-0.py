class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Make text2 the shorter string to minimize space
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        n = len(text2)
        prev = [0] * (n + 1)

        for c1 in text1:
            curr = [0] * (n + 1)
            for j, c2 in enumerate(text2, start=1):
                if c1 == c2:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[n]