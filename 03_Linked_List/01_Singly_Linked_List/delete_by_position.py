# delete_by_position.py
from linked_list import SinglyLinkedList

def delete_by_position(ll, position):
    if not ll.head:  # If the list is empty
        print("List is empty, nothing to delete.")
        return

    # If the position to be deleted is the head node
    if position == 0:
        ll.head = ll.head.next
        return

    current_node = ll.head
    current_position = 0

    while current_node and current_position < position - 1:
        current_node = current_node.next
        current_position += 1

    # If the position is out of bounds
    if not current_node or not current_node.next:
        print(f"Position {position} is out of range.")
        return

    # Delete the node at the specified position
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
