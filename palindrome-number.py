"""
https://leetcode.com/problems/palindrome-number/

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
 

Constraints:
-231 <= x <= 231 - 1
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numStr = str(x) # "454"
        leftPointer = 0 
        rightPointer = len(numStr) - 1
        
        while leftPointer != rightPointer and leftPointer <= len(numStr) and rightPointer >= 0:
          if numStr[leftPointer] != numStr[rightPointer]:
            return False
          else:
            leftPointer += 1
            rightPointer -= 1

        return True

solution = Solution()
print(solution.isPalindrome(5))
print(solution.isPalindrome(64))
print(solution.isPalindrome(646))
print(solution.isPalindrome(1000000001))
