# Define a Node class, which represents a single element in the linked list
class Node:
    def __init__(self, data):
        # Initialize the node with the given data
        self.data = data
        # Initialize the 'next' pointer to None, which will point to the next node in the list
        self.next = None

# Define a SinglyLinkedList class, which represents the entire linked list
class SinglyLinkedList:
    def __init__(self):
        # Initialize the head of the linked list to None, indicating an empty list
        self.head = None
    
    # Method to print the list
    def print_list(self):
        current = self.head  # Start with the head of the list
        while current:  # Traverse the list while the current node is not None
            print(current.data, end=" -> ")  # Print the data of the current node followed by '->'
            current = current.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the list

    def insert_at_end(ll, data):
        new_node = Node(data)
        if not ll.head:  # If the list is empty, make the new node the head
            ll.head = new_node
            return
        last_node = ll.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Append the new node at the end
