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
      
    def display(self):
      current_node = self.top
      stack_values = []
      
      while current_node:
        stack_values.append(current_node.value)
        current_node = current_node.next
        
      return stack_values
    
my_stack = Stack()

def __main__():
  my_stack.push(10)
  my_stack.push(20)
  my_stack.push(30)
  my_stack.push(40)

  my_stack.display()

  my_stack.pop()

  my_stack.size