class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pop = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            int x=1;
            for (int j=0; j<nums.length; j++) {
                if (j!=i){
                    x*=nums[j];
                }
             
            }
             pop[i]=x;
        }
        return pop;
    }
}  
