# insert_at_index.py

# Step 1: Create a new node with the given data
# Step 2: If the index is 0, update the head of the list

# Step 3: Traverse the list until the position before the specified index (index 2)
# 30   --> 20       --> 10      
# head     current      tail    

# Step :4 :Insert the new node at the desired index
# Point new node's next to current node's next
# 30   --> 20       --> 10      
# head     current      tail    
#                       ^
#                       |
#                       40 new node

# Point current node's next to new node
# 30   --> 20       --> 40       -->  10
# head     current      new node     tail


from linked_list import SinglyLinkedList, Node

def insert_at_index(ll, data, index):    
    new_node = Node(data)    # Creat a new node
    
    # Update head if index = 0
    if index == 0:
        new_node.next = ll.head
        ll.head = new_node
        return
    
    current = ll.head  # Start from the head of the list
    current_index = 0  # Initialize the current index
    
    # Traverse to the node before the specified index
    while current is not None and current_index < index - 1:
        current = current.next
        current_index += 1
  
    # If current is None, the index is out of bounds
    if current is None:
        print("Index out of bounds")
        return    
    
    new_node.next = current.next # Point new node's next to current node's next
    current.next = new_node # Point current node's next to new node

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    insert_at_index(ll, 10, 0)   
    insert_at_index(ll, 20, 0)  
    insert_at_index(ll, 30, 0)  
    insert_at_index(ll, 40, 2) # Example

    ll.print_list()
    # Expected output: 30 -> 20 -> 40 -> 10 -> None
    