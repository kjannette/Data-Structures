
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def get_children(self):
        children = []
        if self.leftChild != None:
            children.append(self.leftChild)
        if self.rightChild != None:
            children.append(self.rightChild)
        return children

class Tree:

    def __init__(self):
        self.root = None

    def set_root(self, key, val):
        self.root = Node(key, val)

    def insert(self, key, val):
        if self.root == None:
            self.set_root(key, val)
        else:
            self.insert_node(self.root, key, val)

    def insert_node(self, currentNode, key, val):

        if key <= currentNode.key:
            if currentNode.leftChild:
                self.insert_node(currentNode.leftChild, key, val)
            else:
                currentNode.leftChild = Node(key, val)

        elif key >= currentNode.key:
            if currentNode.rightChild:
                self.insert_node(currentNode.rightChild, key, val)
            else:
                currentNode.rightChild = Node(key, val)

    def find(self, key, val):
        return self.find_node(self.root, key, val)

    def find_node(self, currentNode, key, val):

        if currentNode is None:
            return False
        elif key == currentNode.key:
            return currentNode.val
        elif key < currentNode.key:
            return self.find_node(currentNode.leftChild, key, val)
        else:
            return self.find_node(currentNode.rightChild, key, val)

# Test
# t = Tree()

# t.insert(1, 5)
# t.insert(2, 4)
# t.insert(3, 3)
# t.insert(4, 19)
# t.insert(5, 31)

# print (t.find(4, None))
