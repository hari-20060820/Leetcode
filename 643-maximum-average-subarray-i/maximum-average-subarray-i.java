class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxs=Double.NEGATIVE_INFINITY;
        if (nums.length==1){
            return nums[0];
        }
        for(int i=0;i<=nums.length-k;i++){
            int s=0;
            for(int j=0;j<k;j++){
                s+=nums[i+j];
            }
            if(s>maxs){
                maxs=s;
            }
            
        }
        return  maxs/k;
    }
}