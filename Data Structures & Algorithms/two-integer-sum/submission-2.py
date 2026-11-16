class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = dict()
        for i, n in enumerate(nums):
            D[n] = (n, i);
        for i, n in enumerate(nums):
            cand = D.get(target - n, None)
            if cand and cand[1] != i:
                return [i, cand[1]]
            
