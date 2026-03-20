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
      
    def pop(self):
      if not self.top:
        return None
      
      else:
        popped_node = self.top
        self.top = self.top.next
        
        popped_node.next = None
        self.size -= 1
        
        return popped_node.value
    
    
my_stack = Stack()