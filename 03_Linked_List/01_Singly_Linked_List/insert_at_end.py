# insert_at_end.py
from linked_list import SinglyLinkedList, Node

def insert_at_end(ll, data):
    new_node = Node(data)
    if not ll.head:  # If the list is empty, make the new node the head
        ll.head = new_node
        return
    last_node = ll.head
    while last_node.next:  # Traverse to the last node
        last_node = last_node.next
    last_node.next = new_node  # Append the new node at the end

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    insert_at_end(ll, 10)
    insert_at_end(ll, 20)
    insert_at_end(ll, 30)
    # Add more operations or display the list as needed

ll.print_list()
# 10 -> 20 -> 30 -> None
