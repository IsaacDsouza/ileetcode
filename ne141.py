#141. Linked List Cycle


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        pos = head
        while pos != None:
            if pos in s:
                return True
            else:
                s.add(pos)
            pos = pos.next
        return False


solution=Solution()
