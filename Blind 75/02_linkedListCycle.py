# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

#  Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# 1. Time complexity: O(n), Space complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False

def create_linked_list(values):
    """Create a linked list from a list of values."""
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def create_linked_list_with_cycle(values, pos):
    """Create a linked list from a list of values and introduce a cycle at position 'pos'."""
    head = ListNode(values[0])
    current = head
    cycle_node = None
    for i, value in enumerate(values[1:], 1):
        current.next = ListNode(value)
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node  # Create a cycle
    return head

def main():
    solution = Solution()

    # Test case 1: No cycle
    values = [3, 2, 0, -4]
    head = create_linked_list(values)
    print(f"Has cycle: {solution.hasCycle(head)}")  # Expected: False

    # Test case 2: Cycle exists
    values = [1, 2]
    head = create_linked_list_with_cycle(values, 0)
    print(f"Has cycle: {solution.hasCycle(head)}")  # Expected: True

    # Test case 3: Single node with cycle
    values = [1]
    head = create_linked_list_with_cycle(values, 0)
    print(f"Has cycle: {solution.hasCycle(head)}")  # Expected: True

    # Test case 4: Single node without cycle
    values = [1]
    head = create_linked_list(values)
    print(f"Has cycle: {solution.hasCycle(head)}")  # Expected: False

if __name__ == "__main__":
    main()
