from linked_list import SinglyLinkedList, Node

def search_in_list(ll, data):
    current = ll.head  # Start from the head of the list
    count = 0
    while current:  # Traverse the list
        if current.data == data:  # If data is found
            print(f'Value {data} in postion {count}')
            return 
        count += 1
        current = current.next  # Move to the next node
    print(f'Value {data} not in the list.') 

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    
    # Test the search function
    search_in_list(ll, 20)  
    search_in_list(ll, 30) 
    

# Value 20 in postion 1
# Value 30 not in the list.