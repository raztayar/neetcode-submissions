import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.min_q = heapq.nlargest(k, nums)
        heapq.heapify(self.min_q)

    def add(self, val: int) -> int:
        if len(self.min_q) < self.K:
            heapq.heappush(self.min_q, val)
        elif val > self.min_q[0]:
            heapq.heappop(self.min_q)
            heapq.heappush(self.min_q, val)
        
        return self.min_q[0]
