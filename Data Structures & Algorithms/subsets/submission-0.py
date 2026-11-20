class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def subsets_helper(i):
            if i == len(nums):
                res.append([])
                return
            
            subsets_helper(i+1)

            for j in range(len(res)):
                cpy = res[j].copy()
                cpy.append(nums[i])
                res.append(cpy)
            
            return
        
        subsets_helper(0)
        return(res)