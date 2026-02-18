class Solution {
    public int mySqrt(int x) {
        
        int l=1;
        int r=x;
        int mid;
        int re=0;
        if(x==1 || x==0)
        {
            return x;
        }
       
        while(l<=r)
        {
           
            mid=l+(r-l)/2;//(mid*mid)>x) logically right but more computatin stuff reducve it 

            if( mid > x /mid){ 
                r=mid-1;
            }

            else {
                l=mid+1;
                re=mid;
            }
        }
        return re;
    }
}