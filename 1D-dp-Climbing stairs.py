#MEMO
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            l = helper(i+1)
            r = helper(i+2)
            memo[i] = l+r
            return l+r
        return helper(0)

#TABULATION

dp = [-1] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

#SPACE OPTIMISATION

prev2 = 1
prev = 1

for i in range(2, n+1):
  cur_i = prev2 + prev
  prev2 = prev
  prev = cur_i

print(prev)
