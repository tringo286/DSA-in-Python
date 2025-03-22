# insert_at_index.py
from linked_list import SinglyLinkedList, Node

def insert_at_index(ll, data, index):
    # Step 1: Create a new node with the given data
    new_node = Node(data)
    
    # Step 2: If the index is 0, update the head of the list
    if index == 0:
        new_node.next = ll.head
        ll.head = new_node
        return
    
    current = ll.head  # Start from the head of the list
    current_index = 0  # Initialize the current index
    
    # Step 3: Traverse the list until the position before the specified index
    while current is not None and current_index < index - 1:
        current = current.next
        current_index += 1
  
    # If current is None, the index is out of bounds
    if current is None:
        print("Index out of bounds")
        return
    
    # Step :4 :Insert the new node at the desired index
    new_node.next = current.next
    current.next = new_node

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    insert_at_index(ll, 10, 0)   # Insert 10 at index 0 (beginning)
    insert_at_index(ll, 20, 1)   # Insert 20 at index 1
    insert_at_index(ll, 30, 1)   # Insert 30 at index 1 (between 10 and 20)

    ll.print_list()
    # Expected output: 10 -> 30 -> 20 -> None
