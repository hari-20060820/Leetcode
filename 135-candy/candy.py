class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #Mountains problem solving method , where i kept up=peak, some changes , check with some materials
        n=len(ratings)
        up=0
        peak=0
        down=0
        total=1
        for i in range(1,n):
            
            if(ratings[i]>ratings[i-1]):
                peak+=1
                up=peak+1
                down=0
                total+=(peak+1)
            elif(ratings[i]==ratings[i-1]):
                peak=0
                up=0
                down=0
                total+=1
            else:
                down+=1
                peak=0
                total+=down
                if(down>=up):
                    total+=1
        return total