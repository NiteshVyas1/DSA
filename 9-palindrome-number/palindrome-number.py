class Solution:
    def isPalindrome(self, x: int) -> bool:
        #code
        num = str(x)

        return num == num[::-1]
        