class Solution {
        int i;
        int j;
        int max = 0;
    
    public int lengthOfLongestSubstring(String s) {
                HashSet<Character> longestString  = new HashSet<>();
        
        while(j<s.length()){
            if(!longestString.contains(s.charAt(j))){
                longestString.add(s.charAt(j));
                j++;
                max = Math.max(max, longestString.size());
                
            }else{
                longestString.remove(s.charAt(i));
                i++;
            }
        }
        return max;
        
    }
    
}  
        
 
