"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
 
Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 
Constraints:
0 <= x <= 231 - 1
"""

# Runtime: 2064 ms
# Memory: 13.3 MB
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         i = 1
#         while i > 0:
#             if i * i > x:
#                 return i - 1
#             else:
#                 i += 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x # 9
        mid = x/2 # 4

        if x == 0:
            return 0

        while left < right :
            # i want mid and x/mid to be same
            if x / mid == mid: # 9/4 = 2 
                return mid
            elif x / mid < mid:
                # go lower
                right = mid 
                mid = (right-left) / 2 + 1
            elif x / mid > mid:
                # go higher
                left = mid
                mid = (right-left) / 2 + 1

    
        
solution = Solution()
print(solution.mySqrt(0))
print(solution.mySqrt(9))
print(solution.mySqrt(78))
print(solution.mySqrt(4))
print(solution.mySqrt(67))
