# delete_by_position.py

# 1. Check for empty list: If the linked list is empty, there's nothing to delete.

# 2. Check if the position is valid: Ensure that the position is within the range of the list (i.e., not negative and less than the size of the list).

# 3 .Delete the node at the position:

    # If the position is 0 (head node), adjust the head to the next node.

    # Otherwise, traverse the list to find the node just before the node to be deleted. Adjust the previous node’s next pointer to skip the node to be deleted, effectively removing it from the list.

from linked_list import SinglyLinkedList

def delete_by_position(ll, position):
    if not ll.head:  # If the list is empty
        print("List is empty, nothing to delete.")
        return
    
    # ll.head: This is the current first node in the linked list.  
    # ll.head.next: This refers to the second node in the list
    # By setting ll.head = ll.head.next, you are essentially shifting the head of the list to the second node. This makes the second node the new head of the list  
    if position == 0:
        ll.head = ll.head.next
        return

    current_node = ll.head
    current_position = 0

    while current_node and current_position < position - 1:
        current_node = current_node.next
        current_position += 1

    # If the position is out of bounds
    # When I'm referring to current_node, I mean the pointer/reference to the current node as you traverse the list. This pointer will eventually point to the last node's next, which will be None when you reach the end of the list.
    if not current_node: 
        print(f"Position {position} is out of range.")
        return

    # current_node.next: This points to the node that you want to delete
    # current_node.next.next: This is the node that comes after the one you want to delete.
    # Setting current_node.next = current_node.next.next skips the node to be deleted by pointing the current node to the node after it, removing the reference to the deleted node.
    current_node.next = current_node.next.next

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print("Before deletion:")
    ll.print_list()

    delete_by_position(ll, 1)  # Deleting node at position 1
    print("After deleting node at position 1:")
    ll.print_list()

# Before deletion:
# 10 -> 20 -> 30 -> 40 -> None
# After deleting node at position 1:
# 10 -> 30 -> 40 -> None