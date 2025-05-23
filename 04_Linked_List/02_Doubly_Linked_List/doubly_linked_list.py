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

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end = ' <-> ')
            current_node = current_node.next
        print('None')  

    def insert_at_end(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            return 

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node