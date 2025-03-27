# delete_by_value.py

# 1. Check if the list is empty: If the list is empty (i.e., the head is null), there's nothing to delete.
# 2. Check if the value to delete is in the head node: If the value is found in the head node, we simply move the head to the next node.
from linked_list import SinglyLinkedList

def delete_by_value(ll, value):
    if not ll.head:  # If the list is empty
        print("List is empty, nothing to delete.")
        return

    # If the value to be deleted is the head node
    if ll.head.data == value:
        ll.head = ll.head.next # By setting ll.head = ll.head.next, you are essentially shifting the head of the list to the second node. This makes the second node the new head of the list  
        return

    current_node = ll.head
    while current_node.next:

        # This checks if the data in the next node is equal to the value we're looking for
        if current_node.next.data == value:
            # Setting current_node.next = current_node.next.next skips the node to be deleted by pointing the current node to the node after it, removing the reference to the deleted node.
            current_node.next = current_node.next.next  
            return
        current_node = current_node.next

    print(f"Value {value} not found in the list.")

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print("Before deletion value 20:")
    ll.print_list()

    delete_by_value(ll, 20)
    print("After deleting value 20:")
    ll.print_list()

# Before deletion value 20:
# 10 -> 20 -> 30 -> 40 -> None
# Value 20 not found in the list.
# After deleting value 20:
# 10 -> 30 -> 40 -> None
