class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        r=[]
        digitc={"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"}
        def backt(i,st):
            if len(st)==len(digits):
                r.append(st)
                return 
            for ch in digitc[digits[i]]:
                backt(i+1,st+ch)
            
        if digits:
            backt(0,"")
        return r

        