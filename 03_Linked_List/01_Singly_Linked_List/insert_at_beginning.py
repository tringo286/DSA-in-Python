# insert_at_beginning.py
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
    # Add more operations or display the list as needed

ll.print_list()