from doubly_linked_list import DoublyLinkedList, DoublyNode

def insert_at_end(dll, data):
    new_node = DoublyNode(data) # Create a new node with the given data

    # If the list is empty, the new node becomes the head
    if dll.head is None:
        dll.head = new_node
        return

    # Otherwise, traverse to the last node
    current_node = dll.head
    while current_node.next:
        current_node = current_node.next

    # Insert the new node at the end
    current_node.next = new_node
    new_node.prev = current_node
    

if __name__ == '__main__':
    dll  = DoublyLinkedList()
    insert_at_end(dll, 10)
    insert_at_end(dll, 20)
    dll.print_list() # 10 <-> 20 <-> None