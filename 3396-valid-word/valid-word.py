import re
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word=word.lower()
        reg=r'^[a-z0-9]+$'
        if(len(word)<3):
            return False
        if not any(c in 'aeiou'for c in word ):
            return False
        if not  any(c.isalpha() and c not in  'aeiou'for c in word ):
            return False
        if  not re.match(reg,word):
            return False
        return True
