# Check if an Array is Sorted
# Given an array of size n, the task is to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

# Examples: 

# Input: arr[] = [20, 21, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 78, 98, 99, 97]
# Output: No

# 1. Iterative approach – O(n) Time and O(1) Space
def arraySortedOrNot(arr):
   n = len(arr)

   if n <= 1:
       return True

   for i in range(1, n):
        if arr[i] >= arr[i-1]:
            return True
      
   return False

arr = [7, 7, 7]
if (arraySortedOrNot(arr)): # Yes
    print("Yes")
else:
    print("No")

# 2. Recursive approach – O(n) Time and O(n) Space

# If size of array is zero or one, return true.
# Check last two elements of array, if they are sorted, perform a recursive call with n-1 else, return false.

def arraySortedOrNot(arr, n):

    # Base case
    if (n == 0 or n == 1):
        return True
        
    # Check if present index and index 
    # previous to it are in correct order
    # and rest of the array is also sorted
    # if true then return true else return
    # false
    return (arr[n - 1] >= arr[n - 2] and
            arraySortedOrNot(arr, n - 1))

# Driver code
arr = [ 20, 23, 23, 45, 78, 88 ]
n = len(arr) 

# Function Call
if (arraySortedOrNot(arr, n)): 
    print("Yes")
else:
    print("No")

# Yes