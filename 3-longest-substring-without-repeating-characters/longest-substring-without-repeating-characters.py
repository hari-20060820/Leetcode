class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charindex={}
        start=0
        maxl=0
        for end in range(len(s)):
            if s[end] in charindex and charindex[s[end]]>=start:
                start=charindex[s[end]]+1

            charindex[s[end]]=end
            currentwindow=end-start+1
            maxl=max(maxl,currentwindow)
        return maxl
        