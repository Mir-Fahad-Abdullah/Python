## Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## making a number reverse
        original = x
        reverse = 0
        while x>0:
            last_digit = x%10
            reverse = reverse * 10 + last_digit
            x = x//10
        
        ##checking palindrome
        if reverse == original:
            return True
        else:
            return False