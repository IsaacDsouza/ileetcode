#21. Merge Two Sorted Lists

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        
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
linked_list_head = build_linked_list([1,2,4])
linked_list_head2 = build_linked_list([1,3,4])
merge=solution.mergeTwoLists(linked_list_head,linked_list_head2)
print(merge)
