class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_idx = {ch: i for i, ch in enumerate(s)}
        result: list[int] = []
        end = 0
        size = 0

        for i, ch in enumerate(s):
            end = max(end, last_idx[ch])
            size += 1
            if i == end:
                result.append(size)
                size = 0

        return result