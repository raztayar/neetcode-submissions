import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)

            if -s2 < -s1:
                heapq.heappush(max_heap, s1 - s2)
        
        if max_heap:
            return -max_heap[0]
        
        return 0
            


