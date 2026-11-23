class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step = 0
        two_steps = 0

        for i in range(len(cost) - 1, -1, -1):
            curr = cost[i] + min(one_step, two_steps)
            two_steps = one_step
            one_step = curr

        return min(one_step, two_steps)