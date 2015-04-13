__author__ = 'kochanik'


class Element:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


class LinkedList():
    def __str__(self):
        print(str(self.head.prev))

    def __init__(self):
        self.head = None

    def push(self, value0):
        val = Element(value0)
        if self.head is None:
            self.head = val
        else:
            val1 = self.head
            self.head = val
            self.head.next = val1
            self.head.next.prev = val

    def length(self):
        if not self.head:
            return 0
        length = 1
        current = self.head.next
        while current:
            current = current.next
            length += 1
        return length

    def at(self, index):
        el=self.head
        while index != 0:
            el = el.next
            if el:
                index -= 1
            else:
                raise AttributeError
        return el


