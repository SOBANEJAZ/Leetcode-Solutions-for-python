class Node:
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
N1 = Node(10)
N2 = Node(20)

class LinkedList:
    def __init__(self):
        self.head = None