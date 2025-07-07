#203. Remove Linked List Elements. Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev, cur = dummy, head

        while cur:
            nextn=cur.next
            if cur.val == val:
                prev.next=nextn
            else:
                prev=cur
            cur=nextn
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
linked_list_head = build_linked_list([1,2,6,3,4,5,6])
newll = solution.removeElements(linked_list_head,6)
print(newll)