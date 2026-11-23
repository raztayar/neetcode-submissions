class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [0] * n
        suffix_prod = [0] * n
        
        pre_acc = 1
        suff_acc = 1
        for i in range(n):
            pre_acc *= nums[i]
            prefix_prod[i] = pre_acc

            suff_acc *= nums[n - 1 - i]
            suffix_prod[n - 1 - i] = suff_acc
        
        res = [0] * n

        res[0] = suffix_prod[1]
        res[n - 1] = prefix_prod[n - 2]

        for i in range(1, n-1):
            res[i] = prefix_prod[i - 1] * suffix_prod[i + 1]

        return res