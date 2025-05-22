# insert_at_beginning.py

# Step 1: Create a new node with the given data
# 30        20   -->  10   
# new_node  head      tail

# Step 2: Point the new node's 'next' to the current head of the list
# 30  -->    20   -->  10   
# new_node  head      tail

# Step 2: Update the head of the linked list to point to the new node
# 30  -->    20   -->  10   
# head                tail

from linked_list import SinglyLinkedList, Node

def insert_at_beginning(ll, data):
    new_node = Node(data)   
    new_node.next = ll.head 
    ll.head = new_node      

# Example usage
if __name__ == "__main__":  
    ll = SinglyLinkedList()
    insert_at_beginning(ll, 10)
    insert_at_beginning(ll, 20) 
    insert_at_beginning(ll, 30) # Example
    ll.print_list() # 30 -> 20 -> 10 -> None    