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
    
  def delete(self, data):
    if not self.head:
      return

    if self.head.data == data:
      self.head = self.head.next
      return
    
    current = self.head
    
    while current.next:
      
      if current.next.data == data:
        current.next = current.next.next
        return
      
      current = current.next
      
  def delete_all(self, data):

    while self.head and self.head.data == data:
      self.head = self.head.next

    current = self.head

    while current and current.next:
      if current.next.data == data:
        current.next = current.next.next
      else:
        current = current.next

    
  def search(self, data):
    current = self.head

    while current:
      if (current.data == data):
        return current.data

      current = current.next

    return -1
  
  def get_linkedlist_len(self):
    
    if not self.head:
      return
    
    count = 0
    
    current = self.head
    
    while current:
      count += 1
      current = current.next
      
    return count

    
  def display(self):
    current = self.head
    
    while current:
      print(current.data)
      current = current.next
      
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)

print(my_list.get_linkedlist_len())
