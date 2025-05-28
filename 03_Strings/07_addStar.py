# Insert a character at Multiple Positions

# Given a string str and an array of indices chars[] that describes the indices in the original string where the characters will be added. For this post, let the character to be inserted in star (*). Each star should be inserted before the character at the given index. Return the modified string after the stars have been added.

# Examples: 

# Input: str = "geeksforgeeks", chars = [1, 5, 7, 9]
# Output: g*eeks*fo*rg*eeks
# Explanation: The indices 1, 5, 7, and 9 correspond to the bold characters in "geeksforgeeks".

# Input: str = "spacing", chars = [0, 1, 2, 3, 4, 5, 6]
# Output: "*s*p*a*c*i*n*g"

# 1. Approach - Linear Traversal with Index Tracking    

# Iterate over the string and keep track of the count of the characters in the string so far and whenever your count becomes equal to the element in the array of stars, append a star to the resultant string and move ahead in your star array. 

def addStars(s, stars) :

    # Create a string ans for storing
    # resultant string
    ans = ""
    j = 0

    for i in range(len(s)) :

        # If the count of characters
        # become equal to the stars[j],
        # append star
        if (j < len(stars) and i == stars[j]) :
            ans += '*'
            j += 1
        ans += s[i]
    return ans

string = "geeksforgeeks"
chars = [ 1, 5, 7, 9 ]
ans = addStars(string, chars)

# Printing the resultant string
print(ans) # g*eeks*fo*rg*eeks

# 2. Approach - By Using inbuilt insert function

# In this approach we need to increase the length of orignal string as on insert operation the orignal string get modified and so the target index needs to be increased by 1 so we used k.

# Step-by-step approach:

# The addStars function takes a string s and a vector of integers stars as input.
# It iterates through the stars vector using a for loop.
# For each position specified in the stars vector, it inserts an asterisk (*) at that position in the string s(using insert function).
# we increment the k on insertion because size increases on an insertion operation.
# The updated string is returned.

def addStars(s, stars):
  
    # Iterate through the vector of positions
    k = 0
    for i in range(len(stars)):
      
        # Insert a star at the specified position
        s = s[:stars[i]+k] + "*" + s[stars[i]+k:]
        k += 1
    return s

str = "geeksforgeeks"
chars = [1, 5, 7, 9]
ans = addStars(str, chars)

# Printing the resultant string
print(ans) # g*eeks*fo*rg*eeks