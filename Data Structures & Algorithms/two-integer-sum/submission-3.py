class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {x : i for i, x in enumerate(nums)}

        for i, x in enumerate(nums):
            j = D.get(target - x, -1)
            if j != -1 and j != i:
                return [i, j]