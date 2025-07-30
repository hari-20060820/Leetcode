class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ma=(2**31)-1
        mi=-(2**31)
        s=str(x)
        sum=0
        sign =1
        while x!=0:
            if x<0:
                sign =-1
                x=x*-1
            sum=sum*10+x%10
            x=x//10
        if(sum>=mi and sum<=ma):
            sum=sum*sign
            return sum
        else: 
            return 0
        