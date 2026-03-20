from node import Node

class Stack:
  def __init__(self):
    self.top = None
    self.size = 1
    
  def push(self, data):
    new_node = Node(data)

    if not self.top:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
      self.size += 1
    
    
my_stack = Stack()