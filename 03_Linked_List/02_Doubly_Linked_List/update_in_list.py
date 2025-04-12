from doubly_linked_list import DoublyLinkedList, DoublyNode

def update_in_list(ddl, old_data, new_data):
    current_node = ddl.head
    
    while current_node:
        if current_node.data == old_data:
            current_node.data = new_data
            return         
        current_node = current_node.next
    print(f'{old_data} not found') 

if __name__ == "__main__":
    ddl = DoublyLinkedList()
    ddl.insert_at_end(10)
    ddl.insert_at_end(20)
    ddl.print_list() # 10 <-> 20 <-> None
    update_in_list(ddl, 10, 11)
    ddl.print_list() # 11 <-> 20 <-> None