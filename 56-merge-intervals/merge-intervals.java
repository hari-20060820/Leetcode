class Solution {
    public int[][] merge(int[][] intervals) {
        int[][] a=new int[intervals.length][2];
        int n=intervals.length;
        Arrays.sort(intervals, (a1, b) -> Integer.compare(a1[0], b[0]));
        a[0]=intervals[0];
        int j=0;
        for(int i=1;i<n;i++)
        {
            if(a[j][1]>=intervals[i][0])
            {   
                
                a[j][1]=Math.max(intervals[i][1],a[j][1]);
            }
            else
            {
                
                a[++j]=intervals[i];
            }
        }
        return Arrays.copyOf(a, j + 1);
    }
}