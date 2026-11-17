from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for x in nums:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        
        freqs = nlargest(k, counter.items(), key= lambda a: a[1])

        return [x for x,_ in freqs]