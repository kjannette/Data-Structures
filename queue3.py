class Node(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Queue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def shift(self, value):

        node = Node(value, None, None)

        if self.head == None:
            self.head = node
            self.tail = self.head

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def count(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        a = ""
        b = self.head
        if b != None:
            while b.next != None:
                a += b.value
                b = b.next
            a += b.value
        return a

q = Queue()

q.shift("a")
q.shift("b")
q.shift("c")

print (q)

# q.unshift()

# print ("Queue after unshift operation:", q)
