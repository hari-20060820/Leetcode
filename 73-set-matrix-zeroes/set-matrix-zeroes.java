class Solution {
    public void setZeroes(int[][] matrix) {
        boolean col=true;
        
        for(int i=0;i<matrix.length;i++)
        {
            if(matrix[i][0]==0)
                    {
                        col=false;
                    }
            for(int j=1;j<matrix[0].length;j++)
            {
                if(matrix[i][j]==0)
                {
                   
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                    
                }
            }
        }
         for(int i=matrix.length-1;i>=0;i--)
        {
            for(int j=matrix[0].length-1;j>=1;j--)
            {

                 
                if(matrix[0][j]==0||matrix[i][0]==0)
                {
                     System.out.println(i+","+j);
                    matrix[i][j]=0;
                }
                
            }if(!col)
            {
               
                matrix[i][0]=0;
            }
        }
    }
}