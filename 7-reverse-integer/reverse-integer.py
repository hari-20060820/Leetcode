class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if(x>=0 ):
            s=s[::-1]
            if(int(s)<=(2**31)-1):
                return int(s)
            else:
                return 0
        elif(x<=0 and x>=-(2**31)):
            s=s[0]+s[1:][::-1]
            if(int(s)>=-(2**31)):
                return int(s)
            else:
                return 0
            return int(s)
        
        