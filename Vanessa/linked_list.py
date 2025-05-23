class Node:
    """
    An object for storing a single node for a linked list.
    Models two attributes -data and next_node.
    """

    data = None #holds the data of the node
    next_node = None #holds the reference to the next node

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """Adds new Node containing data at the head of the list
        Takes constant time O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or None if not found
        Takes linear time O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes o(1) but finding the position takes O(n)
        
        Therefore, the overall time complexity is O(n)"""
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index - 1
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or Node if key doesn't exist
        Takes linear time O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current



    def __repr__(self):
        """Returns a string representation of the list
        Takes linear time O(n)
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

                current = current.next_node
            return "->".join(nodes)
            