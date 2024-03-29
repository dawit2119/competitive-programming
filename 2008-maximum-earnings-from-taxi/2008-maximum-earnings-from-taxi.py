class Solution:
    def maxTaxiEarnings(self, n, A):
        dp = [0] * (n + 1)
        A.sort()
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            while A and i == A[-1][0]:
                s, e, t = A.pop()
                dp[i] = max(dp[i], dp[e] + e - s + t)
        return dp[0]        