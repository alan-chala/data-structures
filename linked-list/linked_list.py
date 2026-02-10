from node import Node

class LinkedList():
  def __init__(self):
    self.head = None
    
  def append(self, data):
    new_node = Node(data)
    
    if not self.head:
      self.head = new_node
      return
      
    current = self.head
    
    while current.next:
      current = current.next
      
    current.next = new_node
  
  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def display(self):
    current = self.head
    
    while current:
      print(current.data)
      current = current.next
      
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.prepend(1)

my_list.display()
