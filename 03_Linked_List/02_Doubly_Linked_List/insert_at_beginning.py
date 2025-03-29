from doubly_linked_list import DoublyLinkedList, DoublyNode

def insert_at_beginning(dll, data):
    new_node = DoublyNode(data) # Create a new node

    # If the list is not empty, set the current head's prev to the new node
    if dll.head is not None:
        new_node.next = dll.head
        dll.head.prev = new_node

     # Update head to point to the new node
    dll.head = new_node

if __name__ == '__main__':
    dll = DoublyLinkedList()
    insert_at_beginning(dll, 10)
    insert_at_beginning(dll, 20)
    insert_at_beginning(dll, 30)
    dll.print_list() # 30 <-> 20 <-> 10 <-> None