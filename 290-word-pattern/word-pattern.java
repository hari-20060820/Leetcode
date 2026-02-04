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
            boolean b=hm.containsKey(ch);
            

            if(hm.containsValue(words[i]) && !b)
            {
                return false;
            }

            if(b && !hm.get(ch).equals(words[i]))
            {
                return false;
            }
            else
            hm.put(ch,words[i]);
        }
        return true;
    }
}