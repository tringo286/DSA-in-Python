# 21 Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# 1 -> 2 -> 4 
# 1 -> 3 -> 4 

# 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Intuition
# Think of merging two sorted lists like merging two sorted arrays. The idea is to always take the smallest element available from both lists and add it to the result.

# Approach
# Create a dummy node: This helps in handling the head node smoothly without extra conditions.
# Use two pointers (curr1 and curr2) to traverse both linked lists (list1 and list2).
# Compare the values at the current nodes of both lists:
# Attach the node with the smaller value to the new list.
# Move the pointer of the list from which the node was taken forward.
# Move the temp pointer forward to maintain the merged list.
# After the loop ends, one list might still have remaining nodes:
# Attach the non-empty list directly to the merged list.
# Return dummyNode->next, as dummyNode itself is just a placeholder.

# Complexity
# Time complexity: O(n)
# Space complexity: O(1)    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        temp = dummyNode

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next

        # Attach the remaining nodes
        temp.next = curr1 if curr1 else curr2

        return dummyNode.next

def print_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def create_linked_list(arr):
    dummy = ListNode()
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

if __name__ == "__main__":
    # Create two sorted linked lists from arrays
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])

    # Merge them
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    # Print the merged list
    print("Merged Linked List:")
    print_list(merged)

# Merged Linked List:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None