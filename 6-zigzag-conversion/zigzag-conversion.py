class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a=[""]*numRows
        bo=False
        curr=0
        for c in range(len(s)):
            a[curr]+=s[c]
            if(numRows==1):
                return s
                break
            if (curr==numRows-1 or curr==0):
                bo=not bo
            if(bo):
                curr=curr+1
            else:
                curr=curr-1
                

        return ''.join(a)
        
            


        