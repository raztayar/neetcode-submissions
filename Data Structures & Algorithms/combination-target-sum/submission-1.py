class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_sum = 0
        curr_comb = []

        def combinationSum_helper(i):
            nonlocal curr_sum

            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                curr_comb.append(nums[j])
                curr_sum += nums[j]
                # print(curr_comb)

                if curr_sum == target:
                    res.append(curr_comb.copy())
                    # print("success")
                elif curr_sum < target:
                    combinationSum_helper(j)
                
                curr_comb.pop()
                curr_sum -= nums[j]
            
            return
        
        combinationSum_helper(0)
        return res
            

            
