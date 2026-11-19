class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])

        def to2d(k):
            return (k // n, k % n)
        
        def BinarySearch(l, r):
            if l > r:
                return False
            m = (l + r) // 2
            m1, m2 = to2d(m)

            if matrix[m1][m2] == target:
                return True
            elif matrix[m1][m2] < target:
                return BinarySearch(m+1, r)
            else:
                return BinarySearch(l, m-1)
        
        return BinarySearch(0, n*m - 1)
        
        