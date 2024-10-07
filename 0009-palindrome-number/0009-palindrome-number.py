class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False
        
        # Convert the integer to a string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]
