from linked_list import SinglyLinkedList, Node

def search_in_list(ll, data):
    current = ll.head  # Start from the head of the list
    while current:  # Traverse the list
        if current.data == data:  # If data is found
            return True
        current = current.next  # Move to the next node
    return False  # If the data wasn't found

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    
    # Test the search function
    result = search_in_list(ll, 20)  # Should return True
    print(f"Found 20: {result}")
    
    result = search_in_list(ll, 30)  # Should return False
    print(f"Found 30: {result}")
