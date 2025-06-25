# Camel case of a given sentence

# Given a sentence having lowercase characters, the task is to convert it to Camel Case. In Camel Case, words are joined without spaces, the first word keeps its original case, and each subsequent word starts with an uppercase letter.

# Examples: 

# Input: "i got intern at geeksforgeeks"
# Output: "iGotInternAtGeeksforgeeks"

# Input: "here comes the garden"
# Output: "hereComesTheGarden"

# Approach:

# The idea is to traverse the sentence and each time a space is encountered, remove it and capitalize the next character. We use a flag, capitalizeNext, to track when to capitalize the next character. When a space is encountered, we skip it and set capitalizeNext to true. Once a character is found, we capitalize it and set capitalizeNext back to false.

# Python program to convert given sentence to camel case

def convertToCamelCase(s):
    res = []

    # Flag to indicate when to capitalize the next letter
    capitalizeNext = False

    for i in range(len(s)):

        # If we encounter a space, set the flag to capitalize
        # the next character
        if s[i] == ' ':
            capitalizeNext = True

        # If the flag is set, capitalize the current character
        elif capitalizeNext:
            res.append(s[i].upper())

            # Reset the flag after capitalization
            capitalizeNext = False

        # Otherwise, just add the current character to the result
        else:
            res.append(s[i])

    return ''.join(res)

if __name__ == "__main__":
	s = "i got intern at geeksforgeeks"
	print(convertToCamelCase(s)) # iGotInternAtGeeksforgeeks