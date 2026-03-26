from linked_list import Node

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

def removeElements(head, val):
  dummy = Node(0)
  dummy.next = head

  current = dummy

  while current and current.next:
    if current.next.val == val:
      current.next = current.next.next
    else:
      current = current.next

  return dummy.next
