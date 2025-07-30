class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = (2**31) - 1
        MIN_INT = -(2**31)

        reversed_int = 0
        
        # Determine the sign and work with the absolute value
        sign = 1
        if x < 0:
            sign = -1
            x = -x # Work with the positive version for digit reversal

        while x != 0:
            digit = x % 10  # Get the last digit
            
            # Check for overflow/underflow BEFORE adding the new digit
            # For positive numbers:
            # If reversed_int > MAX_INT // 10, then reversed_int * 10 will definitely overflow.
            # If reversed_int == MAX_INT // 10, then check if adding 'digit' will overflow.
            # (MAX_INT % 10) is 7, so if digit > 7, it overflows.
            if sign == 1 and (reversed_int > MAX_INT // 10 or \
                              (reversed_int == MAX_INT // 10 and digit > 7)):
                return 0
            
            # For negative numbers (when dealing with the positive absolute value):
            # The actual MIN_INT is -2147483648. Its absolute value is 2147483648.
            # MAX_INT // 10 is 214748364.
            # If reversed_int > MIN_INT_ABS // 10 (which is 214748364), it will underflow.
            # If reversed_int == MIN_INT_ABS // 10, then check if adding 'digit' will underflow.
            # (MIN_INT_ABS % 10) is 8, so if digit > 8, it underflows.
            # This check is a bit trickier because we're building a positive `reversed_int`
            # and then applying the negative sign at the end. We need to check against
            # the absolute value of MIN_INT.
            if sign == -1 and (reversed_int > MAX_INT // 10 or \
                              (reversed_int == MAX_INT // 10 and digit > 8)): # 8 because -2147483648 ends in 8
                return 0

            reversed_int = reversed_int * 10 + digit # Build the reversed number
            x //= 10 # Remove the last digit from the original number

        return reversed_int * sign