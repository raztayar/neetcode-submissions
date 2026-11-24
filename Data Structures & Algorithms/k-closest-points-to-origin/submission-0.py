class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def norm(lst: List):
            x, y = lst[0], lst[1]
            return math.sqrt(x**2 + y**2)
        
        PQ = []

        for p in points:
            np = norm(p)
            if len(PQ) < k:
                heapq.heappush_max(PQ, (np, p))
            elif np < PQ[0][0]:
                heapq.heappop_max(PQ)
                heapq.heappush_max(PQ, (np, p))
        
        return [p for _, p in PQ]
