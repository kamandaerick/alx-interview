#!usr/bin/python3
"""This algorithm find the minimum number of
coins for a given total"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] != float('inf') else -1
