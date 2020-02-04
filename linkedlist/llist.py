
# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(<data:{!r}, next({!r})>)'.format(self.data, self.next)


class LList:
    def __init__(self):
        self._head = None
        self._length = 0

    def __len__(self):
        return self._length

    def add(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while True:
                if current.next is None:
                    current.next = new_node
                    break
                else:
                    current = current.next
                    continue
        self._length += 1

    def __repr__(self):
        if self._head:
            return repr(self._head)
        else:
            return '<EMPTY>'

    def remove(self, data):
        if self._head:
            prev = None
            current = self._head
            while current is not None:
                if current.data == data:
                    if prev is not None:
                        prev.next = current.next
                    else:
                        self._head = current.next
                    self._length -= 1
                prev = current
                current = current.next

    def add_by_index(self, data, index):
        prev = None
        current = self._head
        current_index = 0
        if index > self._length - 1 or index < 0:
            raise IndexError("Invalid Index")

        while current_index != index:
            current_index += 1
            prev = current
            current = current.next

        new_current = Node(data)
        new_current.next = current
        if prev is not None:
            prev.next = new_current

        self._length += 1

    def get_by_index(self, index):
        current = self._head
        current_index = 0
        if index > self._length - 1 or index < 0:
            raise IndexError("Invalid Index")

        while current_index != index:
            current_index += 1
            current = current.next

        return current.data
