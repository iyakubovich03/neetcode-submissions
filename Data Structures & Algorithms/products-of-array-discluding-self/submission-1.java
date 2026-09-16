class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] yo = new int[nums.length];
        int l = 1;
        int r= 1;
        for (int i=0; i<nums.length; i++) {
            yo[i]=l;
            l*=nums[i];
        }
        for (int j=nums.length-1; j>=0; j--){
            yo[j]*=r;
            r*=nums[j];
        }
        return yo;
        
    }
}  
