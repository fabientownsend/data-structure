class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return self.head_node is None

    def insert_at_head(self, value):
        new_head = Node(value)

        new_head.next = self.head_node
        self.head_node = new_head

        return self.head_node

    def insert_at_tail(self, value):
        new_tail = Node(value)

        if self.get_head() is None:
            self.head_node = new_tail
            return

        current_node = self.get_head()

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_tail
        return
