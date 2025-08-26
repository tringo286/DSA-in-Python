# Stock Buy and Sell - Multiple Transaction Allowed

# Given an array prices[] of size n denoting the cost of stock on each day, the task is to find the maximum total profit if we can buy and sell the stocks any number of times.

# Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

# Examples:

# Input: prices[] = {100, 180, 260, 310, 40, 535, 695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 - 100 = 210
#                        Buy the stock on day 4 and sell it on day 6 => 695 - 40 = 655
#                        Maximum Profit  = 210 + 655 = 865

# Input: prices[] = {4, 2, 2, 2, 4}
# Output: 2
# Explanation: Buy the stock on day 3 and sell it on day 4 => 4 - 2 = 2
#                        Maximum Profit  = 2

# 1. [Naive Approach] Using Recursion - Exponential Time

# We consider every valid pair (A pair of indexes i and j such that price[i] < price[j] and j > i), we get the profit of the pair as (price[j] - price[i]) and add recursively compute profits for i-1 and j+1. Finally we return the maximum of all profits obtained by all valid pairs.

# Function to find the maximum profit
def maxProfitRec(price, start, end):
    res = 0

    # Consider every valid pair, find the profit with it
    # and recursively find profits on left and right of it
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr = (price[j] - price[i]) + \
                       maxProfitRec(price, start, i - 1) + \
                       maxProfitRec(price, j + 1, end)
                res = max(res, curr)
    return res

# Wrapper function
def maximumProfit(prices):
    return maxProfitRec(prices, 0, len(prices) - 1)

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maximumProfit(prices)) # 865 