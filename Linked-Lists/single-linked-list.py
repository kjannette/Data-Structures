class Node(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

#    def __repr__(self):
#        nval = self.next and self.next.value or None
#        return f"[{self.value}]:{repr(nval)}]"

class List(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):

        node = Node(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin

        else:
            self.end.next = node
            self.end = node

    def pop(self): #pops last item off and returns it
        start = self.begin
        if self.begin == None:
            return None
        elif start.next == None:
            x = start.value
            self.begin = None
            self.end = None
            return x
        else:
            x = self.end
            while start.next != x:
                start = start.next
            start.next = None
            self.end = start
            return x.value

    def return_last(self): #returns ref to last item w/o removing it
        if self.end == None:
            return None
        else:
            node = self.end
            return node.value

    def remove_first(self):
        if self.begin == None:
            return None
        else:
            node = self.begin
            self.begin = node.next
            return node.value

    def remove(self, item):
        node = self.begin
        while node:
            if node.value == item:
                self.begin = node.next
                break
            elif node.next.value == item:
                node.next = node.next.next
                break
            else:
                node = node.next
        return node

    def search(self, item):
        current = self.begin
        found = False
        item = item
        while current != None and not found:
            if current.value == item:
                found = True
            else:
                current = current.next

        return found

    def count(self):
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        a = index
        node = self.begin
        count = 0

        while count != index:
            node = node.next
            #print ("hello")
            count += 1

        return node.value

    def dump(self):
        node = self.begin

        while node:
            if self.end != None:
                print (node.value)
                node = node.next
            else:
                break

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

l.push("a")
l.push("b")
l.push("c")

print (l)

print (l.return_last())

print ("PRINTING LIST AFTER OPERATION:", l)
