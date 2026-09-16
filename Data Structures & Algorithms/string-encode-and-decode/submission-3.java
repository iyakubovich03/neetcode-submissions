class Solution {

    public String encode(List<String> strs) {
    String s ="";
    if (strs.isEmpty()) {
        return null;
    }
for (int i=0; i<strs.size(); i++){
   
    s+=(strs.get(i).length())+"#"+strs.get(i);
    }
    return s;
}

    

    public List<String> decode(String str) {
        if (str!=null){
        List<String> po = new ArrayList<>();
        int i =0;
        while(i<str.length()) {
            int j=i;
            while(str.charAt(j)!='#'){
                j+=1;
            }
            int length= Integer.parseInt(str.substring(i,j));
            po.add(str.substring(j+1,j+1+length));
            i=j+1+length;
        }
        return po;
        }
        else {
            return new ArrayList<>();
        }
    }

}