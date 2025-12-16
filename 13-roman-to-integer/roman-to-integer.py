class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        total=0
        c=0
        p=0
        for i in s[::-1]:
            c=roman[i]
            if c<p :
                p=0
                c=-1*c
            else:
                p=c
            total=total+c
        
        return total

        
        