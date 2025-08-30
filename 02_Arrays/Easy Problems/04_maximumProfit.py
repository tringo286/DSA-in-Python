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

# 2. [Better Approach] Local Minima and Maxima - O(n) Time and O(1) Space

# When the prices are going down, we do not do anything and let the prices go down. When the prices reach a local minimum value (a value after which the prices go up), we buy the stock. When the prices are going up, we let the prices go up and once the prices reach a local maxima, we sell the stock.

# The idea is to traverse the array from left to right and do following.

# Find local minima and then a local maxima.
# Compute the difference between two and add to the result.

# Function to calculate the maximum profit
def maximumProfit(prices):
    n = len(prices)
    lMin = prices[0]  # Local Minima
    lMax = prices[0]  # Local Maxima
    res = 0
  
    i = 0
    while i < n - 1:
      
        # Find local minima
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        
        # Local Maxima
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
      
        # Add current profit
        res += (lMax - lMin)
  
    return res

# Driver Code
if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maximumProfit(prices)) # 865