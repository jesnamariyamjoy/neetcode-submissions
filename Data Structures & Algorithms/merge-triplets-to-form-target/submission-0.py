class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        tx, ty, tz = target
        found_x = found_y = found_z = False

        for a, b, c in triplets:
            if a > tx or b > ty or c > tz:
                continue
            if a == tx:
                found_x = True
            if b == ty:
                found_y = True
            if c == tz:
                found_z = True

        return found_x and found_y and found_z