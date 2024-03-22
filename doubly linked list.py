class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not provided.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        print(f"Element {key} not found in the list.")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
my_doubly_linked_list = DoublyLinkedList()
my_doubly_linked_list.insert_at_beginning(10)
my_doubly_linked_list.insert_at_beginning(20)
my_doubly_linked_list.insert_at_end(30)
my_doubly_linked_list.insert_after(my_doubly_linked_list.head, 25)
print("Doubly Linked List:")
my_doubly_linked_list.display()
my_doubly_linked_list.delete(20)
print("\nDoubly Linked List after deleting 20:")
my_doubly_linked_list.display()
