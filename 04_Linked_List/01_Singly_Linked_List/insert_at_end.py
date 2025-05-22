# insert_at_end.py

# Steps to Insert at End:
# 1. Create a new node with the given data.

# 2. Check if the list is empty: if the head is NULL, make the new node the head.

# 3. Traverse to the last node: start from the head and move until you find the last node (next pointer is NULL).

# 4. Attach the new node to the last node by setting its next pointer to the new node.
# 10    -> 20        30
# head     tail      new_node

# 5. Set the new node’s next to NULL (as it's the last node).
# 10    -> 20   ->   30
# head               tail

from linked_list import SinglyLinkedList, Node

def insert_at_end(ll, data):
    new_node = Node(data)

    if not ll.head:  # If the list is empty, make the new node the head
        ll.head = new_node
        return
    
    temp_node = ll.head
    while temp_node.next:  # Traverse to the last node
        temp_node = temp_node.next
    temp_node.next = new_node  # Append the new node at the end

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    insert_at_end(ll, 10)
    insert_at_end(ll, 20)
    insert_at_end(ll, 30) # Example  

ll.print_list()
# 10 -> 20 -> 30 -> None
