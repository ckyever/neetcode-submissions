class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        i = len(cost) - 3

        while i >= 0:
            one_step_cost = cost[i] + cost[i+1]
            two_step_cost = cost[i] + cost[i+2]
            cost[i] = min(one_step_cost, two_step_cost)
            i -= 1

        return min(cost[0], cost[1])