class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        res = 0
        vis = set()

        for right in range(len(s)):

            while s[right] in vis:
                vis.remove(s[left])
                left += 1

            vis.add(s[right])

            res = max(res, right - left + 1)

        return res