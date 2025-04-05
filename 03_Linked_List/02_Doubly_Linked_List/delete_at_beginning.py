from doubly_linked_list import DoublyLinkedList, DoublyNode
from insert_at_end import insert_at_end

def delete_at_beginning(dll):

    if dll.head is None:
        print('Nothing to delete, the list is empty')
        return 
    
    if dll.head.next:
        dll.head = dll.head.next
        dll.head.prev = None
    else:
        dll.head = None  # If there's only one node, set head to None


if __name__ == '__main__':
    dll = DoublyLinkedList()
    insert_at_end(dll, 10)
    insert_at_end(dll, 20)
    insert_at_end(dll, 30)
    delete_at_beginning(dll)
    dll.print_list() # 20 <-> 30 <-> None