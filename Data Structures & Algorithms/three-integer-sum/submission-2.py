class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        n = len(snums)

        res = []

        D = {x : k for k, x in enumerate(snums)}

        for i in range(n):
            if i == 0 or snums[i] != snums[i-1]:
                for j in range(i+1, n):
                    if j == i+1 or snums[j] != snums[j-1]:
                        k = D.get(-(snums[i] + snums[j]), -1)
                        if k != -1 and k > j:
                            res.append([snums[i], snums[j], snums[k]])
        
        return res