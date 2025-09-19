# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Approach 1:

# Intuition
# We need to check if every opening bracket has a corresponding closing bracket in the correct order. A stack is a natural choice because it follows Last-In-First-Out (LIFO), which matches the bracket pairing rule.

# Approach
# Traverse the string character by character.

# If it is an opening bracket ((, [, {), push it onto the stack.

# If it is a closing bracket (), ], }):

# Check if the stack is empty → if yes, return False.

# Otherwise, pop from the stack and ensure the popped element matches the type of closing bracket.

# If not matching, return False.

# At the end, if the stack is empty, return True; otherwise, False.

# Complexity
# Time complexity:
# O(n) — we traverse the string once.

# Space complexity:
# O(n) — in the worst case, all characters are opening brackets stored in the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0

def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        "()",           # True
        "()[]{}",       # True
        "(]",           # False
        "([)]",         # False
        "{[]}",         # True
        "",             # True (edge case: empty string)
    ]
    
    for s in test_cases:
        print(f"Is '{s}' valid? {solution.isValid(s)}")

if __name__ == "__main__":
    main()

        