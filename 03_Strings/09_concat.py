# Concatenation of Two Strings

# String concatenation is the process of joining two strings end-to-end to form a single string.

# Examples

# Input: s1 = “Hello”, s2 = “World”
# Output: “HelloWorld”
# Explanation: Joining “Hello” and “World” results in “HelloWorld”.

# Input: s1 = “Good”, s2 = “Morning”
# Output: “GoodMorning”
# Explanation: Joining “Good” and “Morning” results in “GoodMorning”

# 1. Using + Operator

s1 = "Hello, "
s2 = "World!"

# Concatenating the strings
res = s1 + s2

print(res) # Hello, World!

# 2. Write your Own Method

# Create an empty result string.
# Traverse through s1 and append all characters to result.
# Traverse through s2 and append all characters to result

def concat(s1, s2):
    res = ''
    
    # Append s1 to res
    for c in s1:
        res += c
    
    # Append s2 to res
    for c in s2:
        res += c
    
    return res

s1 = 'Hello, '
s2 = 'World!'

# Call the function to concatenate the strings
res = concat(s1, s2)

print(res) # Hello, World!