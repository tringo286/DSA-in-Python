# Program to find Smallest and Largest Word in a String

# Given a string, find the minimum and the maximum length words in it. 

# Examples: 
# Input : "This is a test string"
# Output : Minimum length word: a
#          Maximum length word: string
# Input : "GeeksforGeeks A computer Science portal for Geeks"
# Output : Minimum length word: A
#          Maximum length word: GeeksforGeeks

# 1. Method 1:

# The idea is to keep a starting index si and an ending index ei. 

# si points to the starting of a new word and we traverse the string using ei.
# Whenever a space or ‘\0’ character is encountered,we compute the length of the current word using (ei - si) and compare it with the minimum and the maximum length so far. 
# If it is less, update the min_length and the min_start_index( which points to the starting of the minimum length word).
# If it is greater, update the max_length and the max_start_index( which points to the starting of the maximum length word).
# Finally, update minWord and maxWord which are output strings that have been sent by reference with the substrings starting at min_start_index and max_start_index of length min_length and max_length respectively.

# Python3 program to find Smallest and 
# Largest Word in a String

# defining the method to find the longest 
# word and the shortest word
def minMaxLengthWords(inp):
    length = len(inp)
    si = ei = 0
    min_length = length
    min_start_index = max_length = max_start_index = 0
    
    # loop to find the length and stating index
    # of both longest and shortest words
    while ei <= length:
        if (ei < length) and (inp[ei] != " "):
            ei += 1
        else:
            curr_length = ei - si
            
            # condition checking for the shortest word
            if curr_length < min_length:
                min_length = curr_length
                min_start_index = si
                
            # condition for the longest word 
            if curr_length > max_length:
                max_length = curr_length
                max_start_index = si
            ei += 1
            si = ei
            
    # extracting the shortest word using 
    # it's starting index and length     
    minWord = inp[min_start_index : 
                  min_start_index + min_length]
    
    # extracting the longest word using 
    # it's starting index and length     
    maxWord = inp[max_start_index : max_length]
    
    # printing the final result
    print("Minimum length word: ", minWord)
    print ("Maximum length word: ", maxWord)  

# Using this string to test our code
a = "GeeksforGeeks A Computer Science portal for Geeks"
minMaxLengthWords(a) 

# Minimum length word: A
# Maximum length word: 

# Method 2: By Using Regular Expressions

# In this approach we uses regular expressions to find words in a given input string and iterates through them. It keeps track of the smallest and largest words based on their lengths and prints them.

# First, Define a regular expression pattern to match words.
# Then, Create iterators to search for words within the input string.
# Initialize variables to store the smallest and largest words.
# Iterate through the words in the string.
# Check if the current word is smaller than the smallest word.
# Check if the current word is larger than the largest word .
# At the end ,print the smallest and largest words.

import re

# Function to find the smallest and largest words in a string using regular expressions
def find_smallest_largest_words_regex(input_str):
    # Define a regular expression pattern to match words
    word_regex = r'\b\w+\b'
    words = re.findall(word_regex, input_str)

    # Initialize variables to store the smallest and largest words
    smallest_word = ""
    largest_word = ""

    # Iterate through the words in the string
    for word in words:
        # Check if the current word is smaller than the smallest word found so far
        if len(word) < len(smallest_word) or not smallest_word:
            smallest_word = word

        # Check if the current word is larger than the largest word found so far
        if len(word) > len(largest_word):
            largest_word = word

    # Print the smallest and largest words
    print("Minimum length word:", smallest_word)
    print("Maximum length word:", largest_word)

# Input string
input_str = "This is a test string"

# Call the function to find and display the smallest and largest words
find_smallest_largest_words_regex(input_str)

# Minimum length word: a
# Maximum length word: string

# Method 3: Using Stack

# In this approach, we will push all the words one by one into a char stack and check for the max as well as min length for every word on the basis of that we will print the Minimum length word and Maximum length word.

# Time complexity: O(n), n is length of string.
# Auxiliary Space: O(m), m is the length of the longest word.

def smallest_and_largest_word(string):
    # Variables to store the smallest and largest words
    min_word = ""
    max_word = ""
    # Temporary variable to store each word
    temp = ""
    # Loop through the characters of the string
    i = 0
    while i < len(string):
        if string[i] != ' ':
            # Push characters onto the stack until a space is encountered
            temp += string[i]
        else:
            # When a space is encountered, compare the length of the current word
            # with the smallest and largest words found so far
            if min_word == "" or len(temp) < len(min_word):
                min_word = temp
            if max_word == "" or len(temp) > len(max_word):
                max_word = temp
            # Reset the temporary variable for the next word
            temp = ""
        i += 1

    # Compare the length of the last word with the smallest and largest words found so far
    if min_word == "" or len(temp) < len(min_word):
        min_word = temp
    if max_word == "" or len(temp) > len(max_word):
        max_word = temp

    # Store the smallest and largest words
    return min_word, max_word

# Main function


def main():
    string = "GeeksforGeeks A computer Science portal for Geeks"
    # Call the function to find the smallest and largest words
    min_word, max_word = smallest_and_largest_word(string)
    # Print the results
    print("Minimum length word:", min_word)
    print("Maximum length word:", max_word)


if __name__ == "__main__":
    main()

# Minimum length word: A
# Maximum length word: GeeksforGeeks