import re
class Solution(object):
    
        

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=(2**31)-1 
        pattern=r'^\s*([+-]?\d+)'
        val=re.match(pattern,s)
        if(val):
            valu= int(val.group(1))
            if(valu>m):
                return m
            elif(valu<-m ):
                return -(m+1)
            else:
                return valu
        else:
            return 0
        
        
        