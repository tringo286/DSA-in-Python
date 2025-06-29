# Count of substrings that start and end with 1 in given Binary String
# Given a binary string, count the number of substrings that start and end with 1. 

# Examples:

# Input: "00100101"
# Output: 3
# Explanation: three substrings are "1001", "100101" and "101"

# Input: "1001"
# Output: 1
# Explanation: one substring "1001"

# 1. Count of substrings that start and end with 1 in given Binary String using Nested Loop:

# Time Complexity: O(N2), 
# Auxiliary Space: O(1)

# A Simple Solution is to run two loops. Outer loops pick every 1 as a starting point and the inner loop searches for ending 1 and increments count whenever it finds 1.

# A simple Python 3 program to count number of
# substrings starting and ending with 1

def countSubStr(st, n):

    # Initialize result
    res = 0

   # Pick a starting point
    for i in range(0, n):
        if (st[i] == '1'):

            # Search for all possible ending point
            for j in range(i+1, n):
                if (st[j] == '1'):
                    res = res + 1

    return res


# Driver program to test above function
st = "00100101"
list(st)
n = len(st)
print(countSubStr(st, n), end="") # 3

# 2. Count of substrings that start and end with 1 in a given Binary String using Subarray count:

# We know that if count of 1's is m, then there will be m * (m - 1) / 2 possible subarrays.

# Follow the steps to solve the problem:

# Count the number of 1's. Let the count of 1's be m. 
# Return m(m-1)/2 

def countSubStr(st, n):

    # Count of 1's in input string
    m = 0

    # Traverse input string and
    # count of 1's in it
    for i in range(0, n):
        if (st[i] == '1'):
            m = m + 1

    # Return count of possible
    # pairs among m 1's
    return m * (m - 1) // 2


# Driver program to test above function
st = "00100101"
list(st)
n = len(st)
print(countSubStr(st, n), end="") # 3