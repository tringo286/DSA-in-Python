from linked_list import SinglyLinkedList, Node

def update_in_list(ll, old_data, new_data):
    current = ll.head  # Start from the head of the list
    while current:  # Traverse the list
        if current.data == old_data:  # If the node with the old data is found
            current.data = new_data  # Update the node's data           
        current = current.next  # Move to the next node  

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    print('Before update:')
    ll.print_list()

    # Test the update function
    update_result = update_in_list(ll, 20, 25)  # Should return True
  
    print('Before update:')
    ll.print_list()
