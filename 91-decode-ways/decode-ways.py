class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            if s[i-1]!="0":
                dp[i]+=dp[i-1]
            two=int(s[i-2:i])
            if (10 <= two <= 26):
                dp[i]+=dp[i-2]
        return dp[n]
"""LeetCode 91 - Decode Ways (DP Algorithm)

1. Define State
   dp[i] = Number of ways to decode the first i characters.

2. Create DP Array
   dp = [0] * (n + 1)

3. Base Cases
   dp[0] = 1                  # Empty string
   dp[1] = 1 if s[0] != '0' else 0

4. Traverse from i = 2 to n

   a) Check One Digit
      If s[i-1] != '0'
          dp[i] += dp[i-1]

   b) Check Two Digits
      num = int(s[i-2:i])
      If 10 <= num <= 26
          dp[i] += dp[i-2]

5. Return
   dp[n]"""