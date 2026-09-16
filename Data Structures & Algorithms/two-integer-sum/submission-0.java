class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> po = new HashMap<Integer,Integer>();
        for (int i=0; i <nums.length; i++){
            int cur = nums[i];
            int dif = target-cur;

            if (po.containsKey(dif))
            return new int[] {po.get(dif),i};


            po.put(nums[i],i);
        }   
       return new int[0];

        }     
    }

