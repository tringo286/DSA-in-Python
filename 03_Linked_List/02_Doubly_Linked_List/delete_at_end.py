from doubly_linked_list import DoublyLinkedList, DoublyNode
from insert_at_end import insert_at_end

def delete_at_end(dll):
    if dll.head is None:
        print('Nothing to delete, the list is empty')
        return 
    
    # If there is only one node
    if dll.head.next is None:
        dll.head = None  
        return

    # Traverse to the last node      
    current_node = dll.head        
    while current_node.next:
        current_node= current_node.next

    # Remove the last node
    current_node.prev.next = None 
    current_node.prev = None # Remove the last node
        
 
if __name__ == '__main__':
    dll = DoublyLinkedList()
    insert_at_end(dll, 10)
    insert_at_end(dll, 20)
    insert_at_end(dll, 30)
    delete_at_end(dll)
    dll.print_list() # 10 <-> 20 <-> None