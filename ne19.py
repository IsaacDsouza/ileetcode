#19. Remove Nth Node From End of List. Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return "->".join(result)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while right and n>0:
            right = right.next
            n-=1
        
        while right:
            left=left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

solution = Solution()
linked_list_head = build_linked_list([1, 2, 3, 4, 5])
result = solution.removeNthFromEnd(linked_list_head,2)
print(result) 