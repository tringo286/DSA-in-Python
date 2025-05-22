from doubly_linked_list import DoublyLinkedList, DoublyNode
from insert_at_end import insert_at_end

def delete_at_postion(dll, postion):
    if dll.head is None:
        print('Nothing to delete, the list is empty')
        return 
    
    # If there is only one node
    if postion == 0:
        dll.head = None  
        return 
    
    current_node = dll.head
    current_node_position = 0
    while current_node and current_node_position < index - 1:
        current_node = current_node.next

    

if __name__ == '__main__':
    pass