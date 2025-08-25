#24. Swap Nodes in Pairs. Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            next_pair=cur.next.next
            second=cur.next

            second.next=cur
            cur.next=next_pair
            prev.next=second

            prev=cur
            cur=next_pair
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
linked_list_head = build_linked_list([1,2,3,4])
print(solution.swapPairs(linked_list_head))

