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
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # To represent the end of the list