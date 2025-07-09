#160. Intersection of Two Linked Lists. Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null. For example, the following two linked lists begin to intersect at node c1: The test cases are generated such that there are no cycles anywhere in the entire linked structure. Note that the linked lists must retain their original structure after the function returns.
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        lenA,lenB=0,0
        tempA, tempB=headA, headB

        while tempA:
            lenA+=1
            tempA=tempA.next
        while tempB:
            lenB+=1
            tempB=tempB.next
        
        if lenA>lenB:
            for _ in range(lenA-lenB):
                headA=headA.next
        elif lenB>lenA:
            for _ in range(lenB-lenA):
                headB=headB.next
        
        while headA and headB:
            if headA!=headB:
                headA=headA.next
                headB=headB.next
            else:
                return headA
        return None




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
listA = build_linked_list([4,1,8,4,5])
listB = build_linked_list([5,6,1,8,4,5])
print(solution.getIntersectionNode(listA, listB))

