class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap <Character,String> hm =new HashMap<Character,String> ();
        int n =pattern.length();
        String[] words=s.split(" ");
        if(pattern.length() != words.length)
            {
                return false;
            }
        for(int i=0;i<n;i++)
        {
            Character ch =pattern.charAt(i);
            String b=words[i];
            if(hm.containsKey(ch))
            {   
                if(!hm.get(ch).equals(b)) return false;
            }
            else{
                if(hm.containsValue(b)) return false;
                hm.put(ch,b);
            }

            
        }
        return true;
    }
}