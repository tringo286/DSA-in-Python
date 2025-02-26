# delete_by_value.py
from linked_list import SinglyLinkedList

def delete_by_value(ll, value):
    if not ll.head:  # If the list is empty
        print("List is empty, nothing to delete.")
        return

    # If the value to be deleted is the head node
    if ll.head.data == value:
        ll.head = ll.head.next
        return

    current_node = ll.head
    while current_node.next:
        if current_node.next.data == value:
            current_node.next = current_node.next.next  # Bypass the node
            return
        current_node = current_node.next

    print(f"Value {value} not found in the list.")

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print("Before deletion:")
    ll.print_list()

    delete_by_value(ll, 20)
    print("After deleting value 20:")
    ll.print_list()
