class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        DP = [-1] * n

        DP[0] = nums[0]

        DP[1] = max(nums[:2])

        for i in range(2, n):
            DP[i] = max(nums[i] + DP[i-2], DP[i-1])
        
        return DP[n-1]