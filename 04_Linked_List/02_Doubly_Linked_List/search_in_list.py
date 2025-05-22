from doubly_linked_list import DoublyLinkedList, DoublyNode

def search_in_list(dll, data):
    current_node = dll.head  
    while current_node:
        if current_node.data == data:
            return True       
        current_node = current_node.next
    return False

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    print(search_in_list(dll, 10)) # True