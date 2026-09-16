class Solution {
    public int[] topKFrequent(int[] nums, int k) {
           HashMap<Integer,Integer> pop = new HashMap<>();
        List<Integer>[] y = new List[nums.length+1];
        for (int i=0; i<nums.length+1; i++){ //fills up the whole list array wth array lists
            y[i]= new ArrayList<Integer>();
        }
        for (int j =0; j<nums.length; j++){ //fills hashmap with number as key n value as number of time it coccurs
            pop.put(nums[j],1 + (pop.containsKey(nums[j])? pop.get(nums[j]) : 0));
        }
        for (HashMap.Entry<Integer,Integer> entry : pop.entrySet()) {// iterates over hashmap and adds values to array n the index(is the freqnucy) while the output is an array list
            y[entry.getValue()].add(entry.getKey()); // at this point you have an array with the frequency n the value is an array list with ponetially several vlaues
        }
        int[] z = new int[k];
        int index =0;
        for (int i=y.length-1; i>0 && index<k; i--) {
            for (int lol:y[i]) {
                if (!(y[i].isEmpty())){//checks if empty
                    z[index]=lol;
                    index++;
                    if (index == k){
                        return z;
                    }

                }
            }

        }
    return z;

    }
}
