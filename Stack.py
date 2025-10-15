class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class Stack:
	def __init__(self):
		self.top = None

	def push(self, element):
		new_node = Node(element)
		new_node.next = self.top
		self.top = new_node
	def pop(self):
		if self.top is None:
			print("Stack Underflow")
			return -1  # Return a sentinel value indicating error
		element = self.top.data
		self.top = self.top.next
		return element

	def peek(self):
		if self.top is None:
			print("Stack is empty")
			return -1  # Return a sentinel value indicating error
		return self.top.data
