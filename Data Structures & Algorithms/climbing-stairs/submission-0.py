class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [-1] * (n + 1)

        def fill_DP():
            DP[n] = 1
            DP[n-1] = 1
            for i in range(n - 2 , -1, -1):
                DP[i] = DP[i+1] + DP[i+2]
        
        fill_DP()
        return DP[0]

        