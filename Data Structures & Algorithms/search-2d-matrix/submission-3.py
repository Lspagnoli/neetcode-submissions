class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def helper(l: int, h: int, i: int) -> bool:

            m = (l + h) // 2
            

            if i >= len(matrix) or l > h:
                return False

            
            if target > matrix[i][h]:
                return helper(0, len(matrix[i])-1, i+1)
            elif matrix[i][m] == target:
                return True
            elif matrix[i][m] < target:
                return helper(m+1, h, i)
            elif matrix[i][m] > target:
                return helper(l, m-1, i)
            
        return helper(0, len(matrix[0])-1, 0)