class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        DP = [-1] * (n+1)

        DP[n] = 0
        DP[n-1] = cost[n-1]

        def fill_DP():
            for i in range(n - 2, -1, -1):
                DP[i] = cost[i] + min(DP[i+1], DP[i+2])
        
        fill_DP()

        return min(DP[0], DP[1])