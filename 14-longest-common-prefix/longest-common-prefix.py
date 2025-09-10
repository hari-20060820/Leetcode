class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        i=0
        res=""
        if(len(strs)==1 or len(strs[0])==0):
            return strs[0]
        while( i<min(len(strs[0]),len(strs[-1]))and strs[0][i]==strs[-1][i]):
            res+=strs[0][i]
            i+=1
        return res