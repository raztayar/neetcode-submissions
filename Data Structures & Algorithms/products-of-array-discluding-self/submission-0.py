class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0
        for x in nums:
            if x == 0:
                zero_count += 1
            if zero_count == 2:
                return [0] * len(nums)
            
            if x != 0:
                total_prod *= x
        
        output = [0] * len(nums)

        for i, x in enumerate(nums):
            if zero_count == 0:
                output[i] = int(total_prod / x)
            elif x == 0:
                output[i] = total_prod
            else:
                output[i] = 0
        
        return output