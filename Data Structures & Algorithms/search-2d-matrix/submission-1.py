class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])

        def to2d(k):
            return (k // n, k % n)
        
        def BinarySearch(l, r):
            while l <= r:
                mid = (l + r) // 2
                m1, m2 = to2d(mid)
            
                if matrix[m1][m2] == target:
                    return True
                elif matrix[m1][m2] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return False
        
        return BinarySearch(0, n*m - 1)
        
        