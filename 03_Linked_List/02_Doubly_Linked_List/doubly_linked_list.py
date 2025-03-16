# Define a Node class for a doubly linked list
class DoublyNode:
    def __init__(self, data):
        # Initialize the node with given data
        self.data = data
        # Initialize the 'next' pointer to None (for next node) and 'prev' pointer to None (for previous node)
        self.next = None
        self.prev = None

# Define a DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        # Initialize the head of the list to None, indicating an empty list
        self.head = None