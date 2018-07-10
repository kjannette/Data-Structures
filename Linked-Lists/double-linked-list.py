class Node(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

#    def __repr__(self):
#        nval = self.next and self.next.value or None
#        pval = self.prev and self.prev.value or None
#        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class List(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, value):

        node = Node(value, None, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            node.prev = self.end
            node.next = None
            self.end.next = node
            self.end = node

    def pop(self):  # removes the last item and returns it
        x = self.end
        start = self.begin
        if self.begin == None:
            return None
        elif start.next == None:
            x = start.value
            self.begin = None
            self.end = None
            return x
        else:
            while start.next != x:
                start = start.next
            start.next = None
            self.end = start
            return x.value

    def unshift(self): # remove first
        if self.begin == None:
            return None
        else:
            node = self.begin
            self.begin = node.next
            node.next.prev = None
            return node.value

    def remove(self, term):  # searches for an item and removes it
        current = self.begin  

        while current:
            if current.value == term:
                if current.next == None:
                    current = current.prev
                    current.next = None
                elif current.prev is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    self.begin = current.next
                    current.next.prev = None

            current = current.next

    def first(self):  #returns reference to first item w/o removing it
        node = self.begin
        if node.prev == None:
            return node.value
        else:
            print ("Error: first node's prev not set to None")

    def last(self):  #returns reference to last item w/o removing it
        node = self.end
        if node.next == None:
            return node.value
        else:
            print ("Error: last node's prev not set to None")

    def count(self):
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):

        node = self.begin
        count = 0
        while count != index:
            node = node.next
            #print ("hello")
            count += 1

        return node.value

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not." 

        if self.begin:
            assert self.begin.prev == None, "Begin.prev not None"
            assert self.end.next == None, "end.next not None"

    def __str__(self):
        a = ""
        b = self.begin
        if b != None:
            while b.next != None:
                a += b.value
                b = b.next
            a += b.value
        return a

l = List()

# Test Data

# l.push("a")
# l.push("b")
# l.push("c")

# print (l)

# print (l.remove("a"))

# print (l)

# print (l.get('c'))
