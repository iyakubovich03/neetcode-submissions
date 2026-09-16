class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
  HashMap<String,List<String>> ans = new HashMap<>();
    for (String s : strs ) {
        int[] temp = new int[26];
        for (char c : s.toCharArray()) {
            temp[c -'a']++;
        }
        String pop = Arrays.toString(temp);
        if (!(ans.containsKey(pop))) {
            ans.put(pop,new ArrayList<>());
        }
        ans.get(pop).add(s);
    }
        
    return new ArrayList<>(ans.values());
    }
}
