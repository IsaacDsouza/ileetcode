#Add two huge integers represented as linked lists (each node stores 4-digit numbers, from 0 to 9999)

#The most significant chunk is at the head

#Return the result in the same linked list format

#Everything must be implemented inside solution(a, b) (and the class ListNode is already provided in the background)

#eg. a=[9876, 5432, 1999] and b=[1,8001], o/p solution(a,b) = [9876, 5434, 0].
#explanation: 987654321999+18001=987654340000

#eg. a=[123, 4, 5] and b=[100, 100, 100], o/p solution(a,b) = [223, 104, 105].
#explanation: 12300040005+10001000100+22301040105

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
    def sumLinkedLists(self, a:Optional[ListNode], b:Optional[ListNode]):
    # Reverse a linked list
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        # Reverse both lists
        a = reverse(a)
        b = reverse(b)

        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while a or b or carry:
            v1 = a.val if a else 0
            v2 = b.val if b else 0

            total = v1 + v2 + carry
            carry = total // 10000

            cur.next = ListNode(total % 10000)
            cur = cur.next

            if a: a = a.next
            if b: b = b.next

        # Reverse the result back
        return reverse(dummy.next)

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
a= build_linked_list([123, 4, 5])
b= build_linked_list([100, 100, 100])

print(solution.sumLinkedLists(a,b))

