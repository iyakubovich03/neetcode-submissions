
class Solution {
    public boolean isAnagram(String s, String t) {
        int x =0;
        int cap =0;
        if (s.length()==t.length()) {
            for (int i =0; i<s.length(); i++) {
                x=0;
                for (int j=0; j<t.length();j++) {
                    if (s.charAt(i)==t.charAt(j)){
                        x++;
                    }
                }
                cap=0;
                for (int z=0; z<s.length(); z++){
                    if (s.charAt(i)==s.charAt(z)){
                        cap++;
                    }
                }
            if (x!=cap) {
                    return false;
                }
        }
        return true;
}
return false;
    }
}
