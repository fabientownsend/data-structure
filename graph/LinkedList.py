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

    def search(self, value):
        current_node = self.get_head()

        while current_node:
            if current_node.value == value:
                return True

            current_node = current_node.next

        return False

    def delete_at_head(self):
        firt_node = self.get_head()

        if firt_node is not None:
            self.head_node = firt_node.next
            firt_node.next = None

        return

    def delete(self, value):
        deleted = False

        if self.is_empty():
            return deleted

        current_node = self.get_head()
        if current_node.value == value:
            self.delete_at_head()
            deleted = True
            return deleted

        previous_node = None
        while current_node:
            if value == current_node.value:
                previous_node.next = current_node.next
                current_node.next = None
                deleted = True
                break

            previous_node = current_node
            current_node = current_node.next

        return deleted

