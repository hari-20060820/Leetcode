class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        r=[]
        if(numRows==1):
            r=[1]
            res.append(r)
            return res
        else:
            for(i) in range(numRows):
                r=[1]
                for(j)in range(1,i):
                    v=res[i-1][j-1]+res[i-1][j]
                    r.append(v)
                if(i!=0):
                    r.append(1)
                res.append(r)
            
            return     res
        