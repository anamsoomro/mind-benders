"""
https://leetcode.com/problems/search-a-2d-matrix/submissions/
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix: 
            # if target is less than the last num in row 
            if target <= row[-1]:
                # search the row
                for num in row:
                    if target == num:
                        return True
                    else:
                        continue
                # if target wasnt in row, its not in matrix
                return False
        return False
      
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(solution.searchMatrix([[1]]), 1)
