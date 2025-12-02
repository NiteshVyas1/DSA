# class Solution:
#     def reverse(self, x: int) -> int:
#         num = str(x)
#         if num[0] == "-":
#             num = num[1::]
#             num = num[::-1] 
#             result = int(num) * -1  
#         else:
#             result = int(num[::-1]) 
        
#         if result > -2**31 and result < 2**31 - 1:
#             return result
#         else:
#             return 0


class Solution:
    def reverse(self, x: int) -> int:
        #dsa 1
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        result = 0
        sign  = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            rem = x % 10
            result = result * 10 + rem
            x //= 10
        
        result *= sign
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
        