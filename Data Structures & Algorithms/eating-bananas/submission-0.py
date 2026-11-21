class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTotalTime(k):
            count  = 0
            for p in piles:
                count += math.ceil(p / k)
            return count
        
        M = max(piles)
        l = 1
        r = M

        while l < r:
            mid = (l + r) // 2
            t = getTotalTime(mid)

            if t > h:
                l = mid + 1
            else:
                r = mid
        
        return l
        