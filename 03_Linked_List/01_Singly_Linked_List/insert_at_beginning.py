# insert_at_beginning.py
from linked_list import SinglyLinkedList, Node

def insert_at_beginning(ll, data):
    new_node = Node(data)   # Step 1: Create a new node with the given data
    new_node.next = ll.head # Step 2: Point the new node's 'next' to the current head of the list
    ll.head = new_node      # Step 3: Update the head of the linked list to point to the new node


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    insert_at_beginning(ll, 10)
    insert_at_beginning(ll, 20) # Add more operations or display the list as needed
    ll.print_list()
    # 20 -> 10 -> None