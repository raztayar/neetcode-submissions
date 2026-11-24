class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []
        rest = set(nums)

        def dfs():
            if not rest:
                res.append(perm.copy())

            for x in nums:
                if x in rest:
                    perm.append(x)
                    rest.remove(x)

                    dfs()

                    rest.add(x)
                    perm.pop()
        
        dfs()
        return res

                    