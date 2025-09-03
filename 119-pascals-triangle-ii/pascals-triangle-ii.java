class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> row=new ArrayList<>();
        List<Integer> r=null;
        List<Integer> pre=null;
        for(int i =0;i<=rowIndex;i++)
        {r=new ArrayList<>();
            for(int j=0;j<=i;j++)
            {
                if(j==0||j==i)
                {
                    r.add(1);
                }
                else
                {
                    r.add(pre.get(j-1)+pre.get(j));
                }
                
               
            }pre=r; row.add(r);
        }
        return row.get(rowIndex);
            }
}