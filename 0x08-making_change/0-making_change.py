#!/usr/bin/python3
""" making change with a tye smallest number of coins """


def makeChange(coins, total):
    """ the function that does it all """
    if total < 0:
        return 0
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
