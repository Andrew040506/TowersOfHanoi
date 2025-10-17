class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class Stack:
    def __init__(self,name):
        self.name = name # name per stack for tower indication
        self.top = None
        
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return -1  # Return a sentinel value indicating error
        element = self.top.data
        self.top = self.top.next
        return element
    
    def peek(self):
        if self.top is None:
            return -1  # Return a sentinel value indicating error
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_items(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        items.reverse()  # bottom to top
        return items
