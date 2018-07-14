class Node(object):

    def __init__(self, value, nxt):

        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):

    def __init__(self):

        self.begin = None
#        self.end = None

    def push(self, obj):

        node = Node(obj, None)

        if self.begin == None:
            self.begin = node
        else:
            oldbegin = self.begin
            self.begin = node
            self.begin.next = oldbegin

    def pop(self): # pops value currently on top of the stack
        if self.begin == None:
            return None
        else:
            node = self.begin
            self.begin = node.next
            return node.value

    def top(self): # returns a reference to the first item w/o removing it
        top = self.begin
        return top.value

    def count(self): #count number of elements
        count = 0
        start = self.begin
        while start:
            count += 1
            start = start.next
        return count

    def dump(self, mark="----"):
        node = self.begin

        while node:
            print (node.value)
            print (mark)
            node = node.next

    def __str__(self):
        a = ""
        b = self.begin
        if b != None:
            while b.next != None:
                a += b.value
                b = b.next
            a += b.value
        return a

s = Stack()

s.push('a')
s.push('b')
s.push('c')
s.push('d')

print (s)

s.pop()

print ("Stack after operation(s):", s)
