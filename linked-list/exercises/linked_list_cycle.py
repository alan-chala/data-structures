# Given head, the head of a linked list, determine if the linked list has a cycle in it.

def hasCycle(head):
  slow = head
  fast = head

  ans = False

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      ans = True
      break

  return ans