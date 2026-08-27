class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        memo={}
        def solve(steps):
            
            if steps ==  0:
                return 1
            if steps < 0:
                return 0
            if steps in memo:
                return memo[steps]
            memo[steps]=solve(steps-1) + solve(steps-2)
            return memo[steps]
        return solve(n)