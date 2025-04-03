from doubly_linked_list import DoublyLinkedList, DoublyNode

def insert_at_position(dll, position, data):
    new_node = DoublyNode(data)

    # Special case: if position is 0, insert at the head
    if position == 0:
        new_node.next = dll.head
        if dll.head:
            dll.head.prev = new_node
        dll.head = new_node
        return
    
    current_node = dll.head
    current_node_position = 0
    while current_node and current_node_position < position - 1:
        current_node = current_node.next
        current_node_position += 1

    if current_node is None:
        print('Postion out of range')
        return 
    
    new_node.next = current_node.next
    new_node.prev = current_node
    
    # We check if current.next to ensure that we're only trying to update the prev pointer of the next node if there is actually a next node. If current.next is None, then the new node is the last node, and there is no need to update any prev pointer of a non-existent next node.
    if current_node.next:
        current_node.next.prev = new_node # Update the previous pointer of the node after current if 

    current_node.next = new_node
    
if __name__ == '__main__':
    dll  = DoublyLinkedList()
    insert_at_position(dll,0, 10)
    insert_at_position(dll,1 ,20)
    dll.print_list() # 10 <-> 20 <-> None