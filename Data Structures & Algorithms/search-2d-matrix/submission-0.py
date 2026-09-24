class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix[0])
        cols = len(matrix)
        total_len = rows*cols
        left = 0
        right = total_len - 1
        while left <= right:
            mid = int((left+right)/2)
            mid_r = int(mid/rows)
            mid_c = int(mid%rows)
            if target == matrix[mid_r][mid_c]:
                return True
            elif target > matrix[mid_r][mid_c]:
                left = mid+1
            else:
                right = mid - 1
        return False
        