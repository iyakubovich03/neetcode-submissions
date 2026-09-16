class Solution {
    public int longestConsecutive(int[] nums) {
        ArrayList<Integer> po= new ArrayList<>();
        for (int i : nums) {
            po.add(i);
        }
        int greatest = 0;
        for (int i=0; i<nums.length; i++) {
            int l = -1;
            int x = 1;
            if (!(po.contains(nums[i]-1))) {
                l=i;
            }
            if (l!= -1) {
                int y = nums[l];
                 while(po.contains(++y)){
                 x++;
            
            }
            
           

            }
            if (x>greatest) {
                greatest = x;
            }
            
        }
        return greatest;
        
    }
}
