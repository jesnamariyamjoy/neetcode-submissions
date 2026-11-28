class Solution:
    def isHappy(self, n: int) -> bool:
        def next_sum(val: int) -> int:
            total = 0
            while val > 0:
                digit = val % 10
                total += digit * digit
                val //= 10
            return total

        slow = n
        fast = next_sum(n)

        while fast != 1 and slow != fast:
            slow = next_sum(slow)
            fast = next_sum(next_sum(fast))

        return fast == 1