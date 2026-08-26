class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        open=['[','(','{']
        pair={"[":"]","(":")","{":"}"}
        if len(s)==1:
            return False
        for i in s:
            if i in open :
                stack.append(i)
            elif stack:
                 s=stack.pop()
                 if pair[s]!=i:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False