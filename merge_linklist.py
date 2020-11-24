'''
Merge two sorted linked lists
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
Consider two sorted linked lists and the merged list below them as an example.
'''


def merge_sorted(head1, head2):
  #TODO: Write - Your - Code
  newHead = None

  while head1 or head2:
    if head1 and head2:
      if head1.data > head2.data:
        if newHead == None:
          newHead = head2
          cur = newHead
        else:
          cur.next = head2
          cur = head2
        head2 = head2.next
      else:
        if newHead == None:
          newHead = head1
          cur = head1
        else:
          cur.next = head1
          cur = head1
        head1 = head1.next
    elif head1 is None:
      cur.next = head2
      cur = head2
      head2 = head2.next
    else:
      cur.next = head1
      cur = head1
      head1 = head1.next

  return newHead
