from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for x in sorted(count):
            needed = count[x]
            if needed == 0:
                continue
            for v in range(x, x + groupSize):
                if count[v] < needed:
                    return False
                count[v] -= needed

        return True